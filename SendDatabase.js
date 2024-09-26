const handleSave=() => {

    const dates={


        nombre:"rauf",
        descripcion:"123"
    }
    sendDataToDatabase(dates)



}


const sendDataToDatabase = async (data) => {
    const url = 'https://lissome-couples.000webhostapp.com/reactNative/conectionDB.php'; // Reemplaza con la URL de tu API
  
    try {
      const response = await fetch(url, {
        method: 'POST', // o 'PUT' si estás actualizando datos
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
      });
  
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
  
      const result = await response.json();
      return result;
    } catch (error) {
      console.error('There was an error!', error);
    }
  };
  
export default handleSave