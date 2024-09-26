import React,{useState} from 'react';
import { View, Text, TextInput, Button,Alert,StyleSheet,ScrollView,ImageBackground,SafeAreaView } from 'react-native';
import { addDatabase } from './connection/connections';
import { GestureHandlerRootView } from 'react-native-gesture-handler';




export default function Register(){
    const [name,setName]= useState("")
    const [ password, setPassword]=useState("")
    const Register=async()=>{
        const database= await addDatabase(name,password)
        console.log(database)
      }
    return (
    
    
        <View style={{ flex: 1, justifyContent: 'center', backgroundColor: '#ecf0f1', padding: 8 }}>
     
     
         <Text style={{ margin: 24, fontSize: 18, fontWeight: 'bold', textAlign: 'center' }}>
           User Register 
         </Text>

         <TextInput
            style={styles.descripcion}
            placeholder="Username"
            value={name}
            onChangeText={(text) => setName(text)}
    />
     
    <TextInput
      style={ styles.descripcion }
      placeholder="Password"
      secureTextEntry
      value={password}
      onChangeText={(text) => setPassword(text)}
    />

        <Button title='masterbutton' onPress={Register}>
        
       </Button>


    
       </View>

       
       
     
       );

}


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
  