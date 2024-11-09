
import { supabase } from "./supabase"
import { Alert } from "react-native"
import { getGlobalData, setGlobalData } from "../userGlobal"


export const databaseConnection=async(username,password)=>{
  
    try{
      const {data,error}=await supabase.from("users").select("*").eq("username",username).eq("password",password)
      //console.log(data)
      if(data.length>0){
        //console.log(data)
        const  date=data[0].username
        console.log("el usuario que agrego es",date)
        setGlobalData("usuario",date)
  
        Alert.alert("usuario encontrado")
        return true
      }
      else{
  
        Alert.alert("usuario no encontrado ")

        return false
      }
     
  
  
    }catch(e){
  
      //console.log("hay un error",e)
  
    }
  
  }

  export const addDatabase=async(username,password)=>{
    try{

      console.log(username,password)
      

      if(username!==''&& password!==''){
        const { data, error } = await supabase
        .from('users')
        .insert([
          { username: username, password: password }
        ])
        if(error){
          console.log("hubo un error",error.message)
          return false

        }else{

          console.log("datos insertados correctamente",data) 
          return true
        }
        
       
      }else{

        console.log("los valores son nnullos")
        return false
      }
   
    }catch(e){

      console.log(e)
      return false
    }
    


  }
  export const addConvesationDatabase=async(messages)=>{
    try{
     
      const usuario=getGlobalData("usuario")

      const conexion= await supabase.from("users").select("id").eq("username",usuario)
      console.log(" la conexion es=",conexion.data[0].id)
      id=conexion.data[0].id
      

      if(messages!=""){
        const { data, error } = await supabase
        .from('users')
        .update([
          { "messages": messages }
        ])
        .eq("id",id)
        if(error){
          console.log("hubo un error",error.message)
          return false

        }else{

          console.log("datos insertados correctamente") 
          return true
        }
        
       
      }else{

        //console.log("los valores son nnullos")
        return false
      }
   
    }catch(e){

      //console.log(e)
      return false
    }
    


  }

  export const getMessages = async () => {
    try {
      const usuario=getGlobalData("usuario")

      
      const { data, error } = await supabase
        .from("users")
        .select("messages")
        .eq("username", usuario);
      

       console.log("information",data)
       console.log("lal ongitod=",data.length)
       console.log("usuario",usuario)
  
      if (error) {
         console.log("hubo un error :(", error);
        return 0;
      } else if (data.length > 0 ) {
       

  
        console.log("si hay datos, los datos son ", data[0].messages);
        let message =data[0].messages
        const parsedMessages = JSON.parse(message);  // Now it's an array of messages

        console.log("Fetched messages:", parsedMessages);
  
        // Set the messages as the state
    

        return parsedMessages;
        
      } else {
         console.log("No messages found.");
        return [];
      }
    } catch (e) {
        console.log("hubo un error aca ",e);
      return 0;
    }
  };
  