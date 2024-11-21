import React, { useState, useRef, useEffect } from 'react';
import { View, TextInput, Button, Text, ScrollView, StyleSheet,TouchableOpacity,Image,ImageBackground  } from 'react-native';
import { addConvesationDatabase, getMessages } from './connection/connections';
import { getGlobalData } from './userGlobal';

const ChatApp = () => {
  const [inputText, setInputText] = useState('');
  const [chatMessages, setChatMessages] = useState([]);
  const [isLoading, setIsLoading] = useState(false);
  const scrollViewRef = useRef();

  const sendMensagges = async (update) => {
    try {
      await addConvesationDatabase(update);
    } catch (e) {
      console.log(e.message);
    }
  };

  const handleMessageSend = () => {
    if (inputText.trim() !== '') {
      const newMessage = { user: 'user', message: inputText, timestamp: new Date().toLocaleTimeString() };
      setIsLoading(true);
      fetchPsychologist(inputText);
      setChatMessages((chatMessages) => {
        const update = [...chatMessages, newMessage];
        sendMensagges(update);
        return update;
      });
      setInputText('');
      scrollToBottom();
    }
  };

  const fetchPsychologist = async (mensaje) => {
    try {
      const response = await fetch('https://bold-haze-51091.pktriot.net/pregunta', {
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
      let separateSubstrings = data.respuesta.replace(/nom_usuario,/, getGlobalData("usuario"));
      sendResponse(separateSubstrings);
      setIsLoading(false);
    } catch (error) {
      console.error('Error con el fetching:', error);
    }
  };

  const sendResponse = (mensaje) => {
    const botResponse = { user: 'bot', message: mensaje || "Lo siento, no entendí eso.", timestamp: new Date().toLocaleTimeString() };
    setChatMessages((chatMessages) => {
      const update = [...chatMessages, botResponse];
      sendMensagges(update);
      return update;
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
        if (dates.length > 0) {
          setChatMessages(dates);
        } else {
          let usuario = getGlobalData("usuario");
          setChatMessages([{ user: "bot", message: `Hola, bienvenido ${usuario}`, timestamp: new Date().toLocaleTimeString() }]);
        }
      } catch (error) {
        console.error("Error fetching messages:", error);
      }
    };

    fetchMessages();
  }, []);

  return (
    <ImageBackground 
      source={require('./images/azul.jpeg')}  // Path to your local image
      style={styles.container}
    >
      <View style={styles.titleContainer}>
        <Text style={styles.title}>Wise Mind Assistant</Text>
      </View>
      <ScrollView
        ref={scrollViewRef}
        contentContainerStyle={styles.scrollViewContent}
        onContentSizeChange={() => scrollToBottom()}
      >
        {chatMessages.map((msg, index) => (
          <View
            key={index}
            style={[
              styles.messageContainer,
              { alignSelf: msg.user === 'user' ? 'flex-end' : 'flex-start' },
            ]}
          >
            <Text
              style={[
                styles.messageText,
                { backgroundColor: msg.user === 'user' ? '#dcf8c6' : '#e5e5ea' },
              ]}
            >
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
          placeholderTextColor="#AAAAAA"
        />
        <TouchableOpacity
          onPress={handleMessageSend}
          activeOpacity={0.8}
        >
          <Image
            source={require('./images/enviar.png')}  // Path to your local image
            style={styles.sendButtonImage}
          />
        </TouchableOpacity>
      </View>
    </ImageBackground>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#4A90E2', // Soft blue
    paddingHorizontal: 10,
    paddingTop: 40, // Added some space from the top of the screen
  },
  titleContainer: {
    backgroundColor: '#4CAF50', // Green background for the title
    padding: 15, // Adjust padding for better spacing
    borderRadius: 10,
    marginBottom: 20,
    marginTop: 0, // Added marginTop to create space from the top
  },
  title: {
    fontSize: 24,
    fontWeight: 'bold',
    color: '#FFFFFF', // White text
    textAlign: 'center',
  },
  scrollViewContent: {
    flexGrow: 1,
    paddingVertical: 10,
  },
  messageContainer: {
    maxWidth: '80%',
    marginVertical: 5,
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
    alignSelf: 'flex-end',
  },
  inputContainer: {
    flexDirection: 'row',
    alignItems: 'center',
    paddingBottom: 10,
  },
  textInput: {
    flex: 1,
    height: 40,
    marginRight: 10,
    paddingHorizontal: 10,
    borderRadius: 20,
    backgroundColor: '#FFFFFF', // White background for the input box
    borderWidth: 1, // Visible border
    borderColor: '#CCCCCC', // Border color
    color: '#000000', // Black text
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
  sendButton: {
    backgroundColor: '#5856D6', // Blue button color
    paddingVertical: 10,
    paddingHorizontal: 20,
    borderRadius: 20,
  },
  sendButtonText: {
    color: '#FFFFFF',
    fontSize: 16,
    fontWeight: 'bold',
  },
  sendButtonImage: {
    width: 50,  // Set the width of the image
    height: 50, // Set the height of the image
   // borderRadius: 25, // Half of the width and height to make it round
    resizeMode: 'contain', // Ensure the image fits within the given dimensions
  },
});

export default ChatApp;
