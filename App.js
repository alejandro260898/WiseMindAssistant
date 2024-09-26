// En tu App.js o en el archivo principal de tu aplicación
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';
import { StyleSheet ,View,Text} from 'react-native';
import MainSecondScreen from './MainSecondScreen';
import ChatApp from './textInput';
import Register from './Register';

import LoginScreen from './LoginScreen';
import TabNavigator from './navigation/tabNavigation';
import PokemonDetails from './api';

const Stack = createStackNavigator();


export default function App() {
  return (
    <NavigationContainer>
      <Stack.Navigator initialRouteName={{ headerShown: false }}>
        
        <Stack.Screen name="login" component={LoginScreen} />
        <Stack.Screen name="MainSecondScreen" component={MainSecondScreen} />
        <Stack.Screen name="chatApp" component={ChatApp} />
        <Stack.Screen name ="Register" component={Register}/>
        <Stack.Screen name="Tab" component={TabNavigator}/>
        <Stack.Screen name="Api" component={PokemonDetails}/>
         
       
      
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

