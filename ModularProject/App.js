// En tu App.js o en el archivo principal de tu aplicación
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';
import { StyleSheet ,View,Text} from 'react-native';

import LoginScreen from './LoginScreen';
import MainScreen from './MainScreen';
import MainSecondScreen from './MainSecondScreen';

import Pizza from './setPizza';


import Area from './viewArea';
import ChatApp from './textInput';



const Stack = createStackNavigator();


const App = () => {
  return (
    <NavigationContainer>
      <Stack.Navigator initialRouteName="MainScreen">
        
        <Stack.Screen name="Login" component={LoginScreen} />

        
        <Stack.Screen name="Pizza" component={Pizza} />
        <Stack.Screen name="Area" component={Area} />
        <Stack.Screen name="ChatApp" component={ChatApp}/>



       
       
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

export default App;
