<template>
  <div>
    <h2>搜尋機票</h2>
    <div>
      <label for="origin">出發地:</label>
      <input type="text" id="origin" v-model="origin" />
    </div>
    <div>
      <label for="destination">目的地:</label>
      <input type="text" id="destination" v-model="destination" />
    </div>
    <div>
      <label for="departDate">出發日期:</label>
      <input type="date" id="departDate" v-model="departDate" />
    </div>
    <div>
      <label for="returnDate">回程日期:</label>
      <input type="date" id="returnDate" v-model="returnDate" />
    </div>
    <button @click="searchFlights">搜尋</button>
    <div v-if="isLoading">搜尋中...</div>
    <div v-else-if="results.length > 0">
      <h2>搜尋結果:</h2>
      <ul>
        <li v-for="result in results" :key="result.id">
          {{ result.origin }} - {{ result.destination }} {{ result.price }}
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      origin: '',
      destination: '',
      departDate: '',
      returnDate: '',
      isLoading: false,
      results: [],
    };
  },
  methods: {
    async searchFlights() {
      this.isLoading = true;
      this.results = [];

      try {
        const response = await axios.get('https://skyscanner-api-url', {
          params: {
            origin: this.origin,
            destination: this.destination,
            departDate: this.departDate,
            returnDate: this.retSurnDate,
          },
        });
        console.log(response);
        this.results = response.data;
      } catch (error) {
        console.error(error);
      }

      this.isLoading = false;
    },
  },
};
</script>