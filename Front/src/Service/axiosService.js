import axios from 'axios';

export const generateItem = async (item) => {
    const formData = new FormData();
      formData.append('item', item);

      const resposta = await axios.post('http://127.0.0.1:5000/generate', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
        timeout: 300000,
      });
      return resposta.data
  };
export const generateItemSurprise = async () => {
    const resposta = await axios.post('http://127.0.0.1:5000/surprise');
    return resposta.data
};