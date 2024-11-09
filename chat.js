import React, { useState, useRef,useEffect } from 'react';
import { View, TextInput, Button, Text, ScrollView, StyleSheet } from 'react-native';
import { addConvesationDatabase,getMessages } from './connection/connections';
import { supabase } from './connection/supabase';
import { getGlobalData } from './userGlobal';

//import { addConvesationDatabase } from './connection/connections';

const ChatApp = () => {
  const [inputText, setInputText] = useState('');
  const [chatMessages, setChatMessages] = useState([]);
  const [messageApi, setMessageApi] = useState('');
  const scrollViewRef = useRef();
  const [isLoading, setIsLoading] = useState(false);


  const sendMensagges=async(update)=>{
    try{

     await addConvesationDatabase(update)


    }catch(e){


      //console.log(e)
    }
  


  }

  const handleMessageSend = () => {
    if (inputText.trim() !== '') {
      let user=getGlobalData("usuario")
      //console.log("El usuario es",user)
      const newMessage = { user: 'user', message: inputText, timestamp: new Date().toLocaleTimeString() };
      setIsLoading(true);
      fetchPsychologist(inputText);
      setChatMessages(chatMessages=>{

        const update=[...chatMessages, newMessage]

      sendMensagges(update)
      return update
    
    });
      console.log("lo que tiene el mesnaje antes de guardarse es=",chatMessages)
      setInputText('');
      scrollToBottom();
      
      
     // sendMensagges()
      

    }
  };


  const fetchPsychologist = async (mensaje) => {
    try {
      const response = await fetch('http://192.168.100.20:5000/pregunta', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ message: mensaje }),
      });

      if (!response.ok) {
        throw new Error('Network response was not ok');
      }

      const data = await response.json();
      let subStrings=data.respuesta.split(" ")
      let longiud=subStrings.length
      for(let i=0; i<longiud; i++){
        if(subStrings[i]==="nom_usuario,"){
          ////console.log("el string tine",subStrings[i])
          let user=getGlobalData("usuario")
          subStrings[i]=user
        }
       
      }
      let separateSubstrings=subStrings.join("  ")
      console.log("el mensaje que me llega es",separateSubstrings)
     
      //setMessageApi(separateSubstrings);
      sendResponse(separateSubstrings);
      setIsLoading(false);
      return separateSubstrings
    } catch (error) {
      console.error('Error con el fetching:', error);
      return 0
    }
  };

  const sendResponse = (mensaje) => {
    
    const botResponse = { user: 'bot', message: mensaje || "Lo siento, no entendí eso.", timestamp: new Date().toLocaleTimeString() };
 
    setChatMessages(chatMessages=>{

      const update=[...chatMessages, botResponse]
    //console.log("new messages", update)
      sendMensagges(update)
    return update
  
  });
    scrollToBottom();
   
  };

  const scrollToBottom = () => {
    scrollViewRef.current.scrollToEnd({ animated: true });
  };
  useEffect(() => {
    const fetchMessages = async () => {
      try {
       
       let dates = await getMessages();
       // let dates = [{"user":"user","message":"hola","timestamp":"11:58:35 AM"},{"user":"user","message":"hola","timestamp":"11:58:39 AM"},{"user":"user","message":"hh","timestamp":"11:58:42 AM"},{"user":"bot","message":"entonces  onda,  ¿qué  tal  va","timestamp":"11:58:42 AM"},{"user":"user","message":"hola","timestamp":"11:58:48 AM"},{"user":"bot","message":"buen  día  ¿en  puedo","timestamp":"11:58:48 AM"},{"user":"user","message":"hola","timestamp":"11:58:51 AM"},{"user":"bot","message":"buen  día  ¿en  puedo","timestamp":"11:58:51 AM"},{"user":"user","message":"hola","timestamp":"12:29:04 PM"},{"user":"user","message":"hola","timestamp":"12:29:08 PM"},{"user":"user","message":"hola","timestamp":"12:29:14 PM"},{"user":"bot","message":"buen  día  ¿en  puedo","timestamp":"12:29:15 PM"},{"user":"user","message":"hola","timestamp":"12:29:18 PM"},{"user":"bot","message":"buen  día  ¿en  puedo","timestamp":"12:29:18 PM"},{"user":"user","message":"hola","timestamp":"12:29:20 PM"},{"user":"bot","message":"buen  día  ¿en  puedo","timestamp":"12:29:21 PM"},{"user":"user","message":"hola","timestamp":"12:29:23 PM"},{"user":"bot","message":"buen  día  ¿en  puedo","timestamp":"12:29:23 PM"},{"user":"user","message":"hola","timestamp":"12:29:25 PM"},{"user":"bot","message":"buen  día  ¿en  puedo","timestamp":"12:29:25 PM"}] 
  
        if (dates.length > 0) {
          setChatMessages(dates);
          //console.log(dates)
        } else {
          console.log("no tiene nada");
          let welcome=[{"user":"bot","message":"Hola , bienvenido ","timestamp": new Date().toLocaleTimeString()}]
          setChatMessages(welcome)
        }
      } catch (error) {
        //console.error("Error fetching messages:", error);
      }
    };
  
    fetchMessages();
  }, []);
  

  return (
    <View style={styles.container}>
      <View style={styles.header}>
        <Text style={styles.headerText}>WiseMindAssistend</Text>
      </View>
      <ScrollView
  ref={scrollViewRef}
  contentContainerStyle={styles.scrollViewContent}
  onContentSizeChange={() => scrollToBottom()}
>
  {chatMessages.map((msg, index) => (
    <View key={index} style={[styles.messageContainer, { alignSelf: msg.user === 'user' ? 'flex-end' : 'flex-start' }]}>
      <Text style={[styles.messageText, { backgroundColor: msg.user === 'user' ? '#dcf8c6' : '#e5e5ea' }]}>
        {msg.message}
      </Text>
      <Text style={styles.timestamp}>{msg.timestamp}</Text>
    </View>
  ))}
  {isLoading && (
    <View style={styles.loadingContainer}>
      <Text style={styles.loadingText}>Pensando...</Text>
    </View>
  )}
</ScrollView>

      <View style={styles.inputContainer}>
        <TextInput
          style={styles.textInput}
          onChangeText={setInputText}
          value={inputText}
          placeholder="Escribe un mensaje..."
          placeholderTextColor="#A9A9A9"
        />
        <Button title="Enviar" onPress={handleMessageSend} color="#25D366" />
      </View>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#EAEAEA', // Light grey background
  },
  header: {
    backgroundColor: '#075E54', // WhatsApp header color
    padding: 15,
    alignItems: 'center',
  },
  headerText: {
    color: '#FFFFFF',
    fontSize: 20,
    fontWeight: 'bold',
  },
  scrollViewContent: {
    flexGrow: 1,
    paddingVertical: 10,
  },
  messageContainer: {
    maxWidth: '80%',
    marginVertical: 5,
    alignSelf: 'flex-start', // Align container to the start
  },
  messageText: {
    fontSize: 16,
    lineHeight: 20,
    padding: 10,
    borderRadius: 20,
    overflow: 'hidden',
  },
  timestamp: {
    fontSize: 12,
    color: '#A9A9A9',
    marginTop: 5,
    alignSelf: 'flex-end', // Align timestamp to the right
  },
  inputContainer: {
    flexDirection: 'row',
    alignItems: 'center',
    paddingHorizontal: 10,
    paddingBottom: 10,
    backgroundColor: '#FFFFFF',
    borderTopWidth: 1,
    borderTopColor: '#E5E5E5',
    borderRadius: 20,
    overflow: 'hidden', // To make the input and button rounded
  },
  textInput: {
    flex: 1,
    height: 40,
    borderColor: '#E5E5E5',
    borderWidth: 1,
    marginRight: 10,
    paddingHorizontal: 10,
    backgroundColor: '#F5F5F5',
    borderRadius: 20,
  },
  loadingContainer: {
    alignSelf: 'flex-start',
    marginVertical: 5,
  },
  loadingText: {
    fontSize: 16,
    color: '#A9A9A9',
    fontStyle: 'italic',
  },
  
});

export default ChatApp;
