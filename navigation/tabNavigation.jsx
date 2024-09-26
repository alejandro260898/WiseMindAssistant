// En tu App.js o en el archivo principal de tu aplicación
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';
import LoginScreen from 'C:/Users/raufa/OneDrive/Escritorio/ImportantThings/clonaciones/ModularProject/LoginScreen.js';
import MainSecondScreen from '../MainSecondScreen';
import React from 'react'
import { View, Text, Settings } from 'react-native';
import MaterialCommunityIcons from "react-native-vector-icons/MaterialCommunityIcons";
import { createBottomTabNavigator } from "@react-navigation/bottom-tabs";
import { useTranslation } from "react-i18next";


import Pizza from '../setPizza';
import Area from '../viewArea';
import ChatApp from '../textInput';

const Tab = createBottomTabNavigator();

export default function TabNavigator() {
    const {t} = useTranslation();
    return (
        <Tab.Navigator
            screenOptions={{
                tabBarActiveTintColor:'#00a3e1',
                tabBarShowLabel: false,
            }}>
            <Tab.Screen
                name = 'LoginScreen'
                component = { LoginScreen }
                options={{ 
                    tabBarLabel: 'Home',
                    tabBarIcon: ({ color, size }) => (
                        <MaterialCommunityIcons name="home-outline" color={color} size={size} />
                    ),
                    headerShown: false
                }} 
            />
             
            <Tab.Screen
                name = 'MainSecondScreen'
                component = { MainSecondScreen }
                options={{ 
                    tabBarLabel: 'MainSecondScreen',
                    tabBarIcon: ({ color, size }) => (
                        <MaterialCommunityIcons name="map-marker-radius" color={color} size={size} />
                    ),
                }} 
            />
            <Tab.Screen
                name = 'Pizza'
                component = { Pizza }
                options={{ 
                    tabBarLabel: 'Pizza',
                    tabBarIcon: ({ color, size }) => (
                        <MaterialCommunityIcons name="facebook-messenger" color={color} size={size} />
                    ),
                    tabBarBadge: 1,
                    tabBarBadgeStyle: { backgroundColor: 'blue' }
                }} 
            />
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
    )
}
