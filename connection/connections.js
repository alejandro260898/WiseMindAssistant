
import { supabase } from "./supabase"
import { Alert } from "react-native"



export const databaseConnection=async(username,password)=>{
  
    try{
      const {data,error}=await supabase.from("usuarios").select("*")
      if(data.length>0){
  
        Alert.alert("usuario encontrado")
        return true
      }
      else{
  
        Alert.alert("usuario no encontrado ")

        return false
      }
     
  
  
    }catch(e){
  
      console.log(e)
  
    }
  
  }

  export const addDatabase=async(username,password)=>{
    try{
      

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

          console.log("datos insertados correctamente") 
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

  export const proof=async()=>{

     try{
      
      const {data,error}=await supabase.from("usuarios").select("*")
      if(error){

        console.log("hubo un error :(",error)
      }else{

        console.log("si hay datos , los datos son ",data)
      }

     }catch(e){

      console.log(e)
     }
    
  }