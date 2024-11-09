import { createClient } from '@supabase/supabase-js'
import * as SecureStore from 'expo-secure-store'
//import { URL, API_KEY } from 'react-native-dotenv';
//import { URL, API_KEY } from '@env';


//console.log(process.env.URL,process.env.API_KEY)
//dconst supabaseURL='http://mystifying-rain-15393.pktriot.net/'
const supabaseURL='http://192.168.100.20:8000'
const supabaseKey='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyAgCiAgICAicm9sZSI6ICJhbm9uIiwKICAgICJpc3MiOiAic3VwYWJhc2UtZGVtbyIsCiAgICAiaWF0IjogMTY0MTc2OTIwMCwKICAgICJleHAiOiAxNzk5NTM1NjAwCn0.dc_X5iR_VP_qT0zsiyj_I_OZ2T9FtRU2BBNWN8Bu4GE'
export const supabase=createClient(supabaseURL,supabaseKey)