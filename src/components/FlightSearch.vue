<template>
    <div>
      <h1>Flight Search</h1>
      <el-form @submit.prevent="searchFlights">
        <el-form-item label="From:">
          <el-cascader v-model="from" :options="airports" @change="handleChange" />
        </el-form-item>
        <el-form-item label="To:">
          <el-cascader v-model="to" :options="airports" @change="handleChange" />
        </el-form-item>
        <el-form-item label="Depart:">
          <el-date-picker v-model="departDate" type="date"></el-date-picker>
        </el-form-item>
        <el-form-item label="Return:">
          <el-date-picker v-model="returnDate" type="date"></el-date-picker>
        </el-form-item>
        <el-form-item label="Passengers:">
          <el-select v-model="passengers" placeholder="Select number of passengers">
            <el-option v-for="num in 10" :key="num" :label="num" :value="num"></el-option>
          </el-select>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" native-type="submit">Search Flights</el-button>
        </el-form-item>
      </el-form>
      <ul>
        <li v-for="flight in flights" :key="flight.id">
          <h3>{{ flight.origin }} to {{ flight.destination }}</h3>
          <p>Depart: {{ flight.departureDate }}</p>
          <p>Return: {{ flight.returnDate }}</p>
          <p>Price: {{ flight.price }}</p>
        </li>
      </ul>
    </div>
    <div class="flightlist">
      <div class="flight"></div>
      <div class="flight"></div>
      <div class="flight"></div>
      <div class="flight"></div>
      <div class="flight"></div>
    </div>
    <router-view></router-view>
  </template>
  
  <script>
  import { ref } from 'vue'
  import { useRouter } from 'vue-router'
  import axios from 'axios'
  
  export default {
    setup() {
      const from = ref('')
      const to = ref('')
      const departDate = ref(new Date().toISOString().substr(0, 10))
      const returnDate = ref('')
      const passengers = ref(1)
      const flights = ref([])
      const router = useRouter()
  
  
      const handleChange = (from) => {
        console.log(from);
      };
      const airports = [{
        value: 'JAPAN',
        label: '日本',
        children: [
          {
            value: 'Tokyo',
            label: '東京都',
            children: [
              {
                value: 'NRT',
                label: '成田機場',
              },
              {
                value: 'HND',
                label: '羽田機場',
              }
            ]
          },
          {
            value: 'Osaka',
            label: '大阪府',
            children: [
              {
                value: 'KIX',
                label: '關西機場',
              },
              {
                value: 'ITM',
                label: '伊丹機場',
              },
              {
                value: 'UKB',
                label: '神戶機場',
              }
            ]
          },
          {
            value: 'Hokkaido',
            label: '北海道',
          },
        ],
      },
      {
        value: 'Taiwan',
        label: '臺灣',
        children: [
          {
            value: 'Taipei',
            label: '台北',
            children: [
              {
                value: 'TPE',
                label: '桃園機場',
              },
              {
                value: 'TSA',
                label: '松山機場',
              }
            ]
          },
          {
            value: 'Kaohsiung',
            label: '高雄',
            children: [
              {
                value: 'KHH',
                label: '小港機場',
              },
            ]
          },
        ],
      },
      ];
      
  
  
      const searchFlights = async () => {
      // Check if from and to airports are selected
      if (!from.value || !to.value) {
        alert('Please select both departure and destination airports.')
        return
      }
      // Check if return date is null
      if (!returnDate.value || !departDate.value) {
        alert('Please select Return date & Depart date.')
        return
      }
      // Check if return date is after depart date
      if (returnDate.value && returnDate.value < departDate.value) {
        alert('Return date must be equal or after depart date.')
        return
      }
      // Check if number of passengers is valid
      if (passengers.value <= 0) {
        alert('Number of passengers must be greater than 0.')
        return
      }

      try {
        // Make an API request to the flight search endpoint
        const response = await axios.post('http://127.0.0.1:8000/flights/', {
          a_city: to.value,
          d_city: from.value,
          a_date: departDate.value,
          dDate: returnDate.value,
          passengers: passengers.value
        });

        print("response")
        print(response)


        // Assuming the API response contains an array of flights
        flights.value = response.data.flights

        // Redirect to the flight search results page
        router.push({ name: 'FlightSearchResults' })
      } catch (error) {
        console.error('Failed to fetch flights:', error)
        alert('An error occurred while fetching flights. Please try again.')
      }
    }
  
      return {
        airports,
        handleChange,
        from,
        to,
        departDate,
        returnDate,
        passengers,
        flights,
        searchFlights
      }
    }
  }
  </script>
  
  <style scoped>
  ul {
    list-style-type: none;
    padding: 0;
  }
  
  li {
    margin: 10px 0;
    padding: 10px;
    border: 1px solid #ddd;
  }
  
  .login {
    display: flex;
    justify-content: flex-end;
    padding: 10px;
  }
  
  .login-button {
    padding: 5px 10px;
    background-color: #ddd;
    border: none;
    border-radius: 4px;
  }
  
  .flight{
    height: 200px;
    background-color: lightgray;
    margin: 10px;
  }
  </style>