// En tu App.js o en el archivo principal de tu aplicación
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';
import LoginScreen from 'C:/Users/raufa/OneDrive/Documentos/GitHub/ModularProject/LoginScreen.js';
import MainSecondScreen from '../MainSecondScreen';
import React from 'react'
import { View, Text, Settings } from 'react-native';
import MaterialCommunityIcons from "react-native-vector-icons/MaterialCommunityIcons";
import { createBottomTabNavigator } from "@react-navigation/bottom-tabs";
import { useTranslation } from "react-i18next";




import Area from '../viewArea';
import ChatApp from '../chat';

const Tab = createBottomTabNavigator();

export default function TabNavigator() {
    const {t} = useTranslation();
    return (
        <NavigationContainer>

        
        <Tab.Navigator
            screenOptions={{
                tabBarActiveTintColor:'#00a3e1',
                tabBarShowLabel: false,
            }}>
       
         
       
            <Tab.Screen
                name = {t("Area")}
                component = { Area }
                options={{ 
                    tabBarLabel: 'Area',
                    tabBarIcon: ({ color, size }) => (
                        <MaterialCommunityIcons name="account-outline" color={color} size={size} />
                    ),
                    headerShown: false
                }} 
            />
           
          

        </Tab.Navigator>
        </NavigationContainer>
    )
}
