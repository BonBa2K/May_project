<template>
  <div>
    <h1>Skyscanner Search</h1>
    <form @submit.prevent="searchFlights">
      <div class="form-group">
        <label for="from">From:</label>
        <autocomplete
          id="from"
          v-model="from"
          :options="airportOptions"
          placeholder="Enter an airport code"
          :filter-by-query="true"
        ></autocomplete>
      </div>
      <div class="form-group">
        <label for="to">To:</label>
        <autocomplete
          id="to"
          v-model="to"
          :options="airportOptions"
          placeholder="Enter an airport code"
          :filter-by-query="true"
        ></autocomplete>
      </div>
      <div class="form-group">
        <label for="departDate">Depart:</label>
        <datepicker v-model="departDate"></datepicker>
      </div>
      <div class="form-group">
        <label for="returnDate">Return:</label>
        <datepicker v-model="returnDate"></datepicker>
      </div>
      <div class="form-group">
        <label for="passengers">Passengers:</label>
        <select v-model="passengers" id="passengers">
          <option v-for="num in 10" :key="num" :value="num">{{ num }}</option>
        </select>
      </div>
      <button type="submit">Search Flights</button>
    </form>
    <ul>
      <li v-for="flight in flights" :key="flight.id">
        <h3>{{ flight.origin }} to {{ flight.destination }}</h3>
        <p>Depart: {{ flight.departureDate }}</p>
        <p>Return: {{ flight.returnDate }}</p>
        <p>Price: {{ flight.price }}</p>
      </li>
    </ul>
  </div>
</template>

<script>
import { ref } from 'vue'
import Autocomplete from 'vue3-autocomplete'
import Datepicker from 'vue3-datepicker'
import airportData from './airport.json'

export default {
  components: {
    Autocomplete,
    Datepicker,
  },
  setup() {
    const from = ref('')
    const to = ref('')
    const departDate = ref(new Date().toISOString().substr(0, 10))
    const returnDate = ref('')
    const passengers = ref(1)
    const flights = ref([])
    const airportOptions = ref(airportData.map(airport => airport.iata_code))

    const searchFlights = () => {
      // Check if from and to airports are selected
      if (!from.value || !to.value) {
        alert('Please select both departure and destination airports.')
        return
      }
      // Check if return date is after depart date
      if (returnDate.value && returnDate.value < departDate.value) {
        alert('Return date must be after depart date.')
        return
      }
      // Check if number of passengers is valid
      if (passengers.value <= 0) {
        alert('Number of passengers must be greater than 0.')
        return
      }
      // implement flight search logic here
    }

    return {
      from,
      to,
      departDate,
      returnDate,
      passengers,
      flights,
      airportOptions,
      searchFlights
    }
  }
}
</script>

<style>
ul {
  list-style: none;
  padding: 0;
}

li {
  border: 1px solid black;
  padding: 1rem;
  margin-bottom: 1rem;
}

.form-group {
  margin-bottom: 1rem;
}

.autocomplete-results {
  position: absolute;
  z-index: 10;
  background-color: #fff;
  border: 1px solid #ccc;
  border-top: none;
  max-height: 200px;
  overflow-y: auto;
}

.autocomplete-result {
  padding: 0.5rem;
  cursor: pointer;
}

.autocomplete-result.highlight {
  background-color: #ccc;
}

.autocomplete-result:first-child {
  border-top: 1px solid #ccc;
}

</style>
