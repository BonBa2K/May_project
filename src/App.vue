<template>
  <div id="app">
    <div>
      <div class="login">
        <el-dropdown v-if="loggedIn">
          <span class="el-dropdown-link" @click="showDropdown">
            {{ username }}
            <el-icon class="el-icon--right">
              <i class="el-icon-arrow-down"></i>
            </el-icon>
          </span>
          <template #dropdown>
            <el-dropdown-menu>
              <el-dropdown-item @click="openSettings">Settings</el-dropdown-item>
              <el-dropdown-item @click="logout">Logout</el-dropdown-item>
            </el-dropdown-menu>
          </template>
        </el-dropdown>
        <el-button v-else class="login-button" @click="showLoginDialog">Login</el-button>
      </div>
      <el-dialog v-model="loginDialogVisible" title="Login" width="30%">
        <el-form>
          <el-form-item label="Username">
            <el-input v-model="username"></el-input>
          </el-form-item>
          <el-form-item label="Password">
            <el-input v-model="password" type="password" show-password></el-input>
          </el-form-item>
          <el-form-item>
            <el-button type="primary" @click="login">Login</el-button>
          </el-form-item>
        </el-form>
      </el-dialog>
    </div>
    <router-view></router-view>
  </div>
</template>

<script>
import { ref } from 'vue'
import VueCookies from 'vue-cookies'
import { useRouter } from 'vue-router'
import axios from 'axios';


export default {
  name: 'App',
  setup() {

    const router = useRouter()
    const loginDialogVisible = ref(false)
    const loggedIn = ref(false)
    const dropdownVisible = ref(false)
    const username = ref(VueCookies.get('username') || '')
    const password = ref(VueCookies.get('password') || '')

    const showLoginDialog = () => {
      loginDialogVisible.value = true
    }

    // const login = () => {
    //   console.log(`Username: ${username.value}, Password: ${password.value}`)
    //   if (username.value === '1234' && password.value === '1234') {
    //     loggedIn.value = true
    //     loginDialogVisible.value = false
    //     //username = username.value
    //     VueCookies.set('username', username.value)
    //     VueCookies.set('password', password.value)
    //     username.value='1234'
    //     router.push({ name: 'FlightSearch' })


    //   } else {
    //     alert('Invalid username or password')
    //   }
    //   // username.value = ''
    //   // password.value = ''
    // }

    const showDropdown = () => {
      dropdownVisible.value = true
    }

    const apiUrl = 'http://127.0.0.1:8000/LogIn/';

const login = () => {
  console.log(`Username: ${username.value}, Password: ${password.value}`);
  
  const requestData = {
    UserName: username.value,
    Password: password.value
  };
  console.log(requestData)

  axios.post(apiUrl, requestData)
    .then(response => {
      if (response.status === 200) {
        loggedIn.value = true;
        loginDialogVisible.value = false;
        VueCookies.set('username', username.value);
        VueCookies.set('password', password.value);
        router.push({ name: 'FlightSearch' });
      } else {
        alert('Invalid username or password');
      }
    })
    .catch(error => {
      console.error('Error:', error);
    });
};

    const openSettings = () => {
      console.log('Open settings')
    }

    const logout = () => {
      loggedIn.value = false
      username.value = ''
      password.value = ''
      VueCookies.remove('username')
      VueCookies.remove('password')
      console.log('Logout')
      router.push('/')
    }

    // Other setup code...

    return {
      loginDialogVisible,
      showLoginDialog,
      username,
      password,
      login,
      showDropdown,
      dropdownVisible,
      logout,
      loggedIn,
      openSettings,
      // Other variables and functions...
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
  justify-content: center;
  padding: 10px;
}

.login-button {
  padding: 5px 10px;
  background-color: #ddd;
  border: none;
  border-radius: 4px;
}
</style><template>
  <div id="app">
    <div>
      <div class="login">
        <el-dropdown v-if="loggedIn">
          <span class="el-dropdown-link" @click="showDropdown">
            {{ username }}
            <el-icon class="el-icon--right">
              <i class="el-icon-arrow-down"></i>
            </el-icon>
          </span>
          <template #dropdown>
            <el-dropdown-menu>
              <el-dropdown-item @click="openSettings">Settings</el-dropdown-item>
              <el-dropdown-item @click="logout">Logout</el-dropdown-item>
            </el-dropdown-menu>
          </template>
        </el-dropdown>
        <el-button v-else class="login-button" @click="showLoginDialog">Login</el-button>
      </div>
      <el-dialog v-model="loginDialogVisible" title="Login" width="30%">
        <el-form>
          <el-form-item label="Username">
            <el-input v-model="username"></el-input>
          </el-form-item>
          <el-form-item label="Password">
            <el-input v-model="password" type="password" show-password></el-input>
          </el-form-item>
          <el-form-item>
            <el-button type="primary" @click="login">Login</el-button>
          </el-form-item>
        </el-form>
      </el-dialog>
    </div>
    <router-view></router-view>
  </div>
</template>

<script>
import { ref } from 'vue'
import VueCookies from 'vue-cookies'
import { useRouter } from 'vue-router'
import axios from 'axios';


export default {
  name: 'App',
  setup() {

    const router = useRouter()
    const loginDialogVisible = ref(false)
    const loggedIn = ref(false)
    const dropdownVisible = ref(false)
    const username = ref(VueCookies.get('username') || '')
    const password = ref(VueCookies.get('password') || '')

    const showLoginDialog = () => {
      loginDialogVisible.value = true
    }

    // const login = () => {
    //   console.log(`Username: ${username.value}, Password: ${password.value}`)
    //   if (username.value === '1234' && password.value === '1234') {
    //     loggedIn.value = true
    //     loginDialogVisible.value = false
    //     //username = username.value
    //     VueCookies.set('username', username.value)
    //     VueCookies.set('password', password.value)
    //     username.value='1234'
    //     router.push({ name: 'FlightSearch' })


    //   } else {
    //     alert('Invalid username or password')
    //   }
    //   // username.value = ''
    //   // password.value = ''
    // }

    const showDropdown = () => {
      dropdownVisible.value = true
    }

    const apiUrl = 'http://127.0.0.1:8000/LogIn/';

const login = () => {
  console.log(`Username: ${username.value}, Password: ${password.value}`);
  
  const requestData = {
    UserName: username.value,
    Password: password.value
  };
  console.log(requestData)

  axios.post(apiUrl, requestData)
    .then(response => {
      if (response.status === 200) {
        loggedIn.value = true;
        loginDialogVisible.value = false;
        VueCookies.set('username', username.value);
        VueCookies.set('password', password.value);
        router.push({ name: 'FlightSearch' });
      } else {
        alert('Invalid username or password');
      }
    })
    .catch(error => {
      console.error('Error:', error);
    });
};

    const openSettings = () => {
      console.log('Open settings')
    }

    const logout = () => {
      loggedIn.value = false
      username.value = ''
      password.value = ''
      VueCookies.remove('username')
      VueCookies.remove('password')
      console.log('Logout')
      router.push('/')
    }

    // Other setup code...

    return {
      loginDialogVisible,
      showLoginDialog,
      username,
      password,
      login,
      showDropdown,
      dropdownVisible,
      logout,
      loggedIn,
      openSettings,
      // Other variables and functions...
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
  justify-content: center;
  padding: 10px;
}

.login-button {
  padding: 5px 10px;
  background-color: #ddd;
  border: none;
  border-radius: 4px;
}
</style>