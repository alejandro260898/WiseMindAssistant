import React from 'react';
import { View, Text, Alert, StyleSheet, TouchableOpacity } from 'react-native';
import { LinearGradient } from 'expo-linear-gradient';

export default function Salir({ navigation }) {
  const handleExit = () => {
    Alert.alert(
      "Salir",
      "¿Estás seguro de que quieres salir de la aplicación?",
      [
        {
          text: "Cancelar",
          style: "cancel",
        },
        {
          text: "Salir",
          onPress: () => {
            navigation.navigate("login");
          },
        },
      ],
      { cancelable: false }
    );
  };

  return (
    <LinearGradient
      colors={['#8e44ad', '#3498db']}
      style={styles.gradientContainer}
    >
      <View style={styles.container}>
        <Text style={styles.title}>¿Deseas Salir?</Text>
        <Text style={styles.description}>
          Por favor confirma si deseas salir de la aplicación.
        </Text>
        <TouchableOpacity style={styles.exitButton} onPress={handleExit}>
          <Text style={styles.exitButtonText}>Salir</Text>
        </TouchableOpacity>
      </View>
    </LinearGradient>
  );
}

const styles = StyleSheet.create({
  gradientContainer: {
    flex: 1,
  },
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    padding: 20,
  },
  title: {
    fontSize: 28,
    fontWeight: 'bold',
    color: '#fff',
    marginBottom: 20,
  },
  description: {
    fontSize: 16,
    color: '#ecf0f1',
    textAlign: 'center',
    marginBottom: 30,
    paddingHorizontal: 20,
  },
  exitButton: {
    backgroundColor: '#e74c3c',
    paddingVertical: 12,
    paddingHorizontal: 50,
    borderRadius: 30,
    alignItems: 'center',
    elevation: 4,
  },
  exitButtonText: {
    fontSize: 18,
    color: '#fff',
    fontWeight: '600',
  },
});
