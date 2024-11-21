import React, { useState } from 'react';

import {
  View,
  Text,
  TextInput,
  Alert,
  StyleSheet,
  TouchableOpacity,
  ImageBackground,
} from 'react-native';
import { addDatabase } from './connection/connections';

export default function Register({ navigation }) {
  const [name, setName] = useState('');
  const [password, setPassword] = useState('');
  const [verPassword, setVerPassword] = useState('');

  const Register = async () => {
    try {
      if (password === verPassword) {
        const database = await addDatabase(name, password);
        if (database) {
          Alert.alert('¡Registro exitoso!', 'Tus datos han sido guardados.', [
            { text: 'OK', onPress: () => navigation.navigate('login') },
          ]);
        } else {
          Alert.alert('Error', 'No se pudo registrar el usuario.');
        }
      } else {
        Alert.alert('Error', 'Las contraseñas no coinciden.');
      }
    } catch (e) {
      console.error(e);
    }
  };

  return (
    
    //<View style={styles.container}>
    <ImageBackground 
      source={require('./images/azul.jpeg')}  // Path to your local image
      style={styles.container}
    >
      <Text style={styles.title}>Create an Account</Text>

      <TextInput
        style={styles.input}
        placeholder="Enter your username"
        value={name}
        onChangeText={(text) => setName(text)}
        placeholderTextColor="#b0b0b0"
      />

      <TextInput
        style={styles.input}
        placeholder="Enter your password"
        secureTextEntry
        value={password}
        onChangeText={(text) => setPassword(text)}
        placeholderTextColor="#b0b0b0"
      />

      <TextInput
        style={styles.input}
        placeholder="Confirm your password"
        secureTextEntry
        value={verPassword}
        onChangeText={(text) => setVerPassword(text)}
        placeholderTextColor="#b0b0b0"
      />

      <TouchableOpacity style={styles.button} onPress={Register}>
        <Text style={styles.buttonText}>Register</Text>
      </TouchableOpacity>

      <Text style={styles.footerText}>
        Already have an account?{' '}
        <Text
          style={styles.footerLink}
          onPress={() => navigation.navigate('login')}
        >
          Log in
        </Text>
      </Text>
      </ImageBackground>
   // </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: '#f6f8fa',
    paddingHorizontal: 20,
  },
  title: {
    fontSize: 28,
    fontWeight: 'bold',
    color: '#2c3e50',
    marginBottom: 30,
    textAlign: 'center',
  },
  input: {
    width: '100%',
    backgroundColor: '#fff',
    borderRadius: 10,
    padding: 15,
    fontSize: 16,
    marginBottom: 15,
    borderWidth: 1,
    borderColor: '#ddd',
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.1,
    shadowRadius: 3,
    elevation: 2,
  },
  button: {
    backgroundColor: '#3498db',
    width: '100%',
    paddingVertical: 15,
    borderRadius: 10,
    alignItems: 'center',
    marginTop: 10,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 3 },
    shadowOpacity: 0.2,
    shadowRadius: 4,
    elevation: 5,
  },
  buttonText: {
    color: '#fff',
    fontSize: 18,
    fontWeight: 'bold',
  },
  footerText: {
    marginTop: 20,
    fontSize: 14,
    color: '#7f8c8d',
  },
  footerLink: {
    color: '#3498db',
    fontWeight: 'bold',
  },
});
