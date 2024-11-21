import React, { useState, useEffect } from "react";
import { View, Text, TextInput, Button, StyleSheet, Alert } from "react-native";
import { getDates } from "./connection/connections";

export default function Editar() {
  const [nombre, setNombre] = useState("");
  const [contrasena, setContrasena] = useState("");

  async function getD() {
    try {
      const dates = await getDates(); // Fetch data
      console.log("Datos obtenidos:", dates);

      if (dates) {
        // Assuming dates contains 'name' and 'password' fields
        setNombre(dates[0].username || ""); 
        setContrasena(dates[0].password || "");
      } else {
        Alert.alert("Sin datos", "No se encontraron datos.");
      }
    } catch (e) {
      console.error(e);
      Alert.alert("Error", "No se pudieron obtener los datos.");
    }
  }

  useEffect(() => {
    getD(); // Fetch data on component load
  }, []);

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Editar Datos</Text>
      <Text style={styles.title}>Nombre</Text>
      <TextInput
        style={styles.input}
        placeholder="Nombre"
        value={nombre}
        onChangeText={(text) => setNombre(text)}
      />

      <TextInput
        style={styles.input}
        placeholder="Contraseña"
        value={contrasena}
        secureTextEntry
        onChangeText={(text) => setContrasena(text)}
      />

      <Button title="Guardar Cambios" onPress={() => Alert.alert("Datos guardados")} color="#3498db" />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: "center",
    alignItems: "center",
    backgroundColor: "#f6f8fa",
    padding: 20,
  },
  title: {
    fontSize: 24,
    fontWeight: "bold",
    marginBottom: 20,
    color: "#2c3e50",
  },
  input: {
    width: "90%",
    backgroundColor: "#fff",
    borderWidth: 1,
    borderColor: "#ccc",
    borderRadius: 8,
    padding: 12,
    fontSize: 16,
    marginVertical: 10,
    elevation: 2,
    shadowColor: "#000",
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.2,
    shadowRadius: 4,
  },
});
