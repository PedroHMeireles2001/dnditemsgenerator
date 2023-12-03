import axios from 'axios';

export const generateItem = async (settings) => {
      const resposta = await axios.get('http://127.0.0.1:5000/generate', {
        timeout: 300000,
        params: settings
      });
      return resposta.data
  };
export const generateItemSurprise = async (settings) => {
  const set = settings
  delete set.item
  const resposta = await axios.get('http://127.0.0.1:5000/generate', {
    timeout: 300000,
    params: set
  });
  return resposta.data
};