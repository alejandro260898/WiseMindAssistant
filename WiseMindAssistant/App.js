
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';
import { StyleSheet ,View,Text,Image} from 'react-native';
import { createBottomTabNavigator } from "@react-navigation/bottom-tabs";
import ChatApp from './chat';
import Register from './Register';
import Principal from './principal';
import LoginScreen from './LoginScreen';
import Salir from './salir';

const Stack = createStackNavigator();
const Tab = createBottomTabNavigator();
const TabNavigation = () => {
  return (
    <Tab.Navigator
      initialRouteName="Principal"
      screenOptions={{
        tabBarLabelStyle: { fontSize: 12, color: '#333' }, // Styling the label
        tabBarStyle: { paddingBottom: 5, height: 60 },     // Extra padding for better alignment
      }}
    >
      <Tab.Screen 
        name="Principal" 
        component={Principal} 
        options={{
          tabBarIcon: () => (
            <View style={{
              width: 30, 
              height: 30, 
              borderRadius: 15, 
              overflow: 'hidden', 
              justifyContent: 'center', 
              alignItems: 'center',
              backgroundColor: '#f2f2f2'  // Background color for round effect
            }}>
              <Image 
                source={require('./images/principal.png')} 
                style={{ width: 20, height: 20 }}
              />
            </View>
          ),
          tabBarLabel: 'Principal', // Customize the label text
        }}
      />
      <Tab.Screen 
        name="chatApp" 
        component={ChatApp} 
        options={{
          tabBarIcon: () => (
            <View style={{
              width: 30, 
              height: 30, 
              borderRadius: 15, 
              overflow: 'hidden', 
              justifyContent: 'center', 
              alignItems: 'center',
              backgroundColor: '#f2f2f2'
            }}>
              <Image 
                source={require('./images/chat.png')} 
                style={{ width: 20, height: 20 }}
              />
            </View>
          ),
          tabBarLabel: 'Chat', 
        }}
      />
      <Tab.Screen 
        name="Ajustes" 
        component={Salir} 
        options={{
          tabBarIcon: () => (
            <View style={{
              width: 30, 
              height: 30, 
              borderRadius: 15, 
              overflow: 'hidden', 
              justifyContent: 'center', 
              alignItems: 'center',
              backgroundColor: '#f2f2f2'
            }}>
              <Image 
                source={require('./images/ajustes.png')} 
                style={{ width: 20, height: 20 }}
              />
            </View>
          ),
          tabBarLabel: 'Settings', 
        }}
      />
    </Tab.Navigator>
  );
};
export default function App() {
  return (
    <NavigationContainer>
      <Stack.Navigator initialRouteName={{ headerShown: false }} screenOptions={{
        tabBarShowLabel: false,  
      }}>
        
        <Stack.Screen name="login" component={LoginScreen} options={{ headerShown: false }} />
        <Stack.Screen name="tab" component={TabNavigation}options={{ headerShown: false }} />
        <Stack.Screen name="Register" component={Register} options={{ headerShown: false }}/>
        <Stack.Screen name="chatApp" component={ChatApp}   options={{ headerShown: false }}/>

      
      </Stack.Navigator>
    </NavigationContainer>
    
    
  );
  
};


const styles = StyleSheet.create({
  root: {
    flex: 1,
    alignItems: 'center',
    justifyContent: 'center',
    backgroundColor: 'whitesmoke'
  }
});

