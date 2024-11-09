import React, { useEffect, useState } from 'react';
import { View, Text, ActivityIndicator, StyleSheet, FlatList, StatusBar } from 'react-native';

const Item = ({ name }) => (
  <View style={styles.item}>
    <Text style={styles.title}>Habilidad: {name}</Text>
  </View>
);

const PokemonDetails = () => {
  const [pokemonData, setPokemonData] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchPokemon = async () => {
      try {
        const response = await fetch('http://10.214.123.59:5000/proof');

        if (!response.ok) {
          throw new Error('Network response was not ok');
        }

        const data = await response.json();
        //console.log(data); 
        
        // Update state with the fetched data
        setPokemonData(data);  // Set the fetched data to state
        setLoading(false);      // Set loading to false after fetching
      } catch (error) {
        //console.error('Error fetching the data:', error);
        setLoading(false);      // Set loading to false even on error
      }
    };

    fetchPokemon(); 
  }, []);

  if (loading) {
    return <ActivityIndicator size="large" color="#0000ff" />;
  }

  return (
    <View style={styles.container}>
      {pokemonData ? (
        <FlatList
          data={pokemonData.habilidades || []} // Assuming `habilidades` is an array in the response
          keyExtractor={(item, index) => index.toString()}
          renderItem={({ item }) => <Item name={item} />}
        />
      ) : (
        <Text>No se encontraron habilidades.</Text>
      )}
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    marginTop: StatusBar.currentHeight || 0,
  },
  title: {
    fontSize: 24,
    fontWeight: 'bold',
    marginBottom: 10,
  },
  item: {
    backgroundColor: '#f9c2ff',
    padding: 20,
    marginVertical: 8,
    marginHorizontal: 16,
  },
  title: {
    fontSize: 32,
  },
});

export default PokemonDetails;
