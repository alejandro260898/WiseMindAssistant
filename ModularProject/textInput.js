import React, { useState, useRef } from 'react';
import { View, TextInput, Button, Text, ScrollView, StyleSheet } from 'react-native';

const ChatApp = () => {
  const [inputText, setInputText] = useState('');
  const [chatMessages, setChatMessages] = useState([]);
  const scrollViewRef = useRef();

  const handleMessageSend = () => {
    if (inputText.trim() !== '') {
      const newMessage = { user: 'user', message: inputText };
      console.log(inputText);
      setChatMessages([...chatMessages, newMessage]);
      setInputText('');
      scrollToBottom();
      
      setTimeout(sendResponse, 1000); // Simulamos una respuesta después de 1 segundo
      console.log('pepe');
          
    }
  };

  const responses = ["Hola", "Buenos días", "¿Cómo estás?", "¿En qué puedo ayudarte?", "Adiós"];

  const sendResponse = () => {
    const randomIndex = Math.floor(Math.random() * responses.length);//funcion de numeros random
    
    const botResponse = { user: 'bot', message: responses[randomIndex] };
    setChatMessages(prevMessages => [...prevMessages, botResponse]);
    scrollToBottom();
  };

  

  const scrollToBottom = () => {
    scrollViewRef.current.scrollToEnd({ animated: true });
  };

  return (
    <View style={styles.container}>
      <ScrollView
        ref={scrollViewRef}
        contentContainerStyle={styles.scrollViewContent}
        onContentSizeChange={() => scrollToBottom()}
      >
        {chatMessages.map((msg, index) => (
          <View key={index} style={[styles.messageContainer, { alignSelf: msg.user === 'user' ? 'flex-end' : 'flex-start' }]}>
            <Text style={[styles.messageText, { backgroundColor: msg.user === 'user' ? '#DCF8C6' : '#E5E5EA' }]}>
              {msg.message}
            </Text>
          </View>
        ))}
      </ScrollView>
      <View style={styles.inputContainer}>
        <TextInput
          style={styles.textInput}
          onChangeText={setInputText}
          value={inputText}
          placeholder="Escribe un mensaje..."
        />
        <Button title="Enviar" onPress={handleMessageSend} />
      </View>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#F5F5F5',
  },
  scrollViewContent: {
    flexGrow: 1,
    paddingVertical: 10,
  },
  messageContainer: {
    maxWidth: '80%',
    marginVertical: 5,
    borderRadius: 8,
    padding: 10,
  },
  messageText: {
    fontSize: 16,
  },
  inputContainer: {
    flexDirection: 'row',
    alignItems: 'center',
    paddingHorizontal: 10,
    paddingBottom: 10,
  },
  textInput: {
    flex: 1,
    height: 40,
    borderColor: 'gray',
    borderWidth: 1,
    marginRight: 10,
    paddingHorizontal: 10,
    backgroundColor: '#FFFFFF',
    borderRadius: 20,
  },
});

export default ChatApp;
