// LoginScreen.js
import React,{useState} from 'react';
import { View, Text, TextInput, Button,Alert,StyleSheet,ScrollView,ImageBackground,SafeAreaView,Image,TouchableOpacity} from 'react-native';
import { getGlobalData } from './userGlobal';

import { databaseConnection,addDatabase,proof } from './connection/connections';


export default function LoginScreen({navigation}){

  const [username, setUsername] = useState('');
  const [password,setPassword]=useState('');
  const [description, setDescription] = useState('');
  const image = require('./images/ps.png')
  



const verification = async()=>{
  const getDates = await databaseConnection(username,password)
  //const getDates=true
    if(getDates){
      Alert.alert("usuario encontrado")
      console.log("el usuario que se guardo es ",getGlobalData("usuario"))
      setPassword("")
      setUsername("")

      navigation.navigate("tab"); 
  
    }
    else{
     

      //console.log("no se puede:(")
    }
}






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
            placeholder="Usuario"
            value={username}
            onChangeText={(text) => setUsername(text)}
          />
          
          <TextInput
            style={styles.input}
            placeholder="Contrasena"
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