// LoginScreen.js
import React,{useState} from 'react';
import { View, Text, TextInput, Button,Alert,StyleSheet,ScrollView,ImageBackground,SafeAreaView } from 'react-native';



const LoginScreen = ({ navigation }) => {

  const [username, setUsername] = useState('');
  const [password,setPassword]=useState('');
  const [description, setDescription] = useState('');
  const image = {uri: 'https://legacy.reactjs.org/logo-og.png'};

 
  const Server = () => {
   
    fetch('https://lissome-couples.000webhostapp.com/reactNative/conectionDB.php')
      .then(response => response.json())
      .then(json => console.log(json))
      .catch(error => console.error('Error:', error)); 
  };


  const piz=()=>{


    navigation.navigate('Pizza');
  }


  const Area=()=>{

    navigation.navigate('Area');
  };

  const inputExample=() => {
    navigation.navigate('ChatApp');


  };

  const handleLogin = () => {

    console.log('Username:', username);
    console.log('Description:', description);
  
    fetch('https://lissome-couples.000webhostapp.com/reactNative/conectionDB.php', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
    })
      .then(response => {
        if (!response.ok) {
          throw new Error(`Network response was not ok - Status: ${response.status}`);
        }
        
        return response.json();
      })
      .then(data => {
      
        const userExists = data.some(user => user.nombre === username && user.descripcion === description);
  
        if (userExists) {
          Alert.alert('Inicio de sesion exitoso');
          navigation.navigate('ChatApp');
        
        } else {
          Alert.alert('Nombre de usuario incorrecto');
       
        }
      })
      .catch(error => {
        console.error('Error:', error.message);
        Alert.alert('Error de red');
      });
    
  };

  return (
    
    
   <View style={{ flex: 1, justifyContent: 'center', backgroundColor: '#ecf0f1', padding: 8 }}>
   
          <Text style={styles.text}>Inside</Text>
 

    <Text style={{ margin: 24, fontSize: 18, fontWeight: 'bold', textAlign: 'center' }}>
      My First Code
    </Text>
  
    <TextInput
      style={styles.descripcion}
      placeholder="Username"
      value={username}
      onChangeText={(text) => setUsername(text)}
    />
     
    <TextInput
      style={ styles.descripcion }
      placeholder="Description"
      //secureTextEntry
      value={description}
      onChangeText={(text) => setDescription(text)}
    />
  
  
    <Button title='Hola' onPress={() => Alert.alert('Hola')} />
    <Button title='Iniciar Sesión' onPress={handleLogin} />

     <Button title='Area'onPress={Area}/>

     <Button title='input' onPress={inputExample}/>
   

   
  </View>

  );
};


const styles = StyleSheet.create({
  image: {
    flex: 1,
    justifyContent: 'center',
  },
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
  loginText: {
    margin: 9,
    borderWidth: 8,
    borderColor: 'red',
    padding: 20,
    fontSize: 20,
    fontWeight: 'bold',
  },
  loginBox: {
    borderWidth: 6,
    borderColor: 'red',
    padding: 20,
    borderRadius: 10,
    width: 300,
  },
  loginBox2:{
    borderWidth:6,
    borderColor:"blue",
    padding:10,
    borderRadius:10,
    width:300,
  
  }
  ,
  input: {
    marginVertical: 10,
    borderWidth: 1,
    borderColor: 'gray',
    padding: 10,
    borderRadius: 5,
  },
  inputContainer:{
    flexDirection:'row',
    justifyContent: 'center',

  },
  container2:{
    padding: 10,
  },
  TextInput:{
    borderWidth: 1,
    borderColor: '#CCCCCC',
    width:'80%',

  }
  ,
  backgroundImage: {
    width: '100%', // Ajusta el tamaño según tus necesidades
    height: 200,   // Ajusta el tamaño según tus necesidades
    resizeMode: 'cover', // Puedes ajustar esto según tus necesidades
  },
  descripcion:{ 
    height: 40, 
    borderColor: 'gray',
    borderWidth: 1,
    marginBottom: 10, 
    paddingLeft: 10


  }
});
export default LoginScreen;
