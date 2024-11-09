import React from 'react';
import { View, Text, Button, Alert, StyleSheet } from 'react-native';

export default function Salir({ navigation }) {
  
  const handleExit = () => {
    Alert.alert(
      "Salir",
      "¿Estás seguro de que quieres salir de la aplicación?",
      [
        {
          text: "Cancelar",
          style: "cancel"
        },
        { 
          text: "Salir", 
          onPress: () => {
            
            navigation.navigate("login"); 
          }
        }
      ],
      { cancelable: false }
    );
  };

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Salir de la Aplicación</Text>
      <Button title="Salir" onPress={handleExit} />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: '#f8f9fa',
  },
  title: {
    fontSize: 24,
    marginBottom: 20,
  }
});
