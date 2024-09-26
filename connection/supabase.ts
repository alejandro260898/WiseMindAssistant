import { createClient } from '@supabase/supabase-js'
import * as SecureStore from 'expo-secure-store'

    console.log(process.env.URL,process.env.API_KEY)
    const supabaseURL=process.env.URL
    const supabaseKey=process.env.API_KEY
    export const supabase=createClient(supabaseURL,supabaseKey)