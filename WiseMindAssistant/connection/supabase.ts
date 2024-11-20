import { createClient } from '@supabase/supabase-js'
import * as SecureStore from 'expo-secure-store'
//import { URL, API_KEY } from 'react-native-dotenv';
//import { URL, API_KEY } from '@env';


//console.log(process.env.URL,process.env.API_KEY)
//dconst supabaseURL='http://mystifying-rain-15393.pktriot.net/'
const supabaseURL='https://abgspujwyujtccknqenr.supabase.co'
const supabaseKey='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImFiZ3NwdWp3eXVqdGNja25xZW5yIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MTA0MzU5NzgsImV4cCI6MjAyNjAxMTk3OH0.NOjPxUVPBYztUlLCl6CBYg9vIrl9I58zD6bolUzqYfs'
export const supabase=createClient(supabaseURL,supabaseKey)