// i've created a function to save the user (rauf)

let globalData = {}; 

export const setGlobalData = (key, value) => {
   
  globalData[key] = value; 
};

export const getGlobalData = (key) => {
  return globalData[key]; 
};
