// LoginScreen.js
import React,{useState} from 'react';
import { View, Text, TextInput, Button,Alert,StyleSheet,ScrollView,ImageBackground,SafeAreaView,Image,TouchableOpacity} from 'react-native';


import { databaseConnection,addDatabase,proof } from './connection/connections';


export default function LoginScreen({navigation}){

  const [username, setUsername] = useState('');
  const [password,setPassword]=useState('');
  const [description, setDescription] = useState('');
  const image = {uri: 'https://legacy.reactjs.org/logo-og.png'};
  

 /*
  const Server = () => {
   
    fetch('https://lissome-couples.000webhostapp.com/reactNative/conectionDB.php')
      .then(response => response.json())
      .then(json => console.log(json))
      .catch(error => console.error('Error:', error)); 
  };
*/


const verification = async()=>{
  const getDates = await databaseConnection(username,password)
    if(getDates){
      Alert.alert("usuario encontrado")
      navigation.navigate("chatApp")
  
    }
    else{

      console.log("no se puede:(")
    }
}

const Register=async()=>{
  try{
    const database= await addDatabase(username,password)
      console.log(database)
  }catch(err){
      console.log(err)

  }

}



///  i can handle the login in this function with, this is other way to connect to the database 
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
    <SafeAreaView style={styles.container}>
      <ImageBackground source={image} style={styles.backgroundImage}>

        {/* Encabezado */}
        <View style={styles.headerContainer}>
          <Text style={styles.headerTitle}>PsicologistApp</Text>
        </View>

        {/* Cuerpo */}
        <View style={styles.loginContainer}>
          <TextInput
            style={styles.input}
            placeholder="Username"
            value={username}
            onChangeText={(text) => setUsername(text)}
          />
          
          <TextInput
            style={styles.input}
            placeholder="Password"
            secureTextEntry
            value={password}
            onChangeText={(text) => setPassword(text)}
          />

          {/* Botones */}
          <TouchableOpacity style={styles.button} onPress={verification}>
            <Text style={styles.buttonText}>Iniciar Sesión</Text>
          </TouchableOpacity>

          <TouchableOpacity style={styles.buttonSecondary} onPress={() => navigation.navigate("Register")}>
            <Text style={styles.buttonText}>Registrarse</Text>
          </TouchableOpacity>

          <TouchableOpacity style={styles.buttonSecondary} onPress={() => navigation.navigate("Api")}>
            <Text style={styles.buttonText}>API Test</Text>
          </TouchableOpacity>
        </View>
      </ImageBackground>
    </SafeAreaView>
  );

};


const styles = StyleSheet.create({
  container: {
    flex: 1,
  },
  backgroundImage: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    resizeMode: 'cover',
  },
  headerContainer: {
    alignItems: 'center',
    marginBottom: 40,
  },
  headerTitle: {
    fontSize: 36,
    fontWeight: 'bold',
    color: '#ffffff',
    textShadowColor: 'rgba(0, 0, 0, 0.75)',
    textShadowOffset: { width: -1, height: 1 },
    textShadowRadius: 10,
  },
  loginContainer: {
    backgroundColor: 'rgba(255, 255, 255, 0.85)',
    borderRadius: 20,
    padding: 20,
    width: '80%',
    alignItems: 'center',
  },
  input: {
    width: '100%',
    height: 50,
    borderColor: '#ccc',
    borderWidth: 1,
    borderRadius: 10,
    paddingHorizontal: 10,
    marginVertical: 10,
    fontSize: 16,
  },
  button: {
    backgroundColor: '#4CAF50',
    borderRadius: 10,
    paddingVertical: 15,
    paddingHorizontal: 50,
    marginVertical: 10,
    width: '100%',
    alignItems: 'center',
  },
  buttonSecondary: {
    backgroundColor: '#FF5722',
    borderRadius: 10,
    paddingVertical: 15,
    paddingHorizontal: 50,
    marginVertical: 10,
    width: '100%',
    alignItems: 'center',
  },
  buttonText: {
    color: '#ffffff',
    fontSize: 18,
    fontWeight: 'bold',
  }
});