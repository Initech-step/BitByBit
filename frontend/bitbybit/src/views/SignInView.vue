
    
<template>
  <div class="container">
    <div class="row justify-content-center align-content-center">
      <div class="col col-6 col-lg-7">

        <main class="form-signin m-auto">
          <form @submit.prevent="signInUser">
            <img class="mb-4 text-center" src="@/assets/b3logo.png" alt="" width="72" height="70">
            <h1 class="h3 mb-3 fw-normal">Please sign in</h1>
        
            <div class="form-floating">
              <input type="email" class="form-control" id="floatingInput" v-model="email" required>
              <label for="floatingInput">Email address</label>
            </div>

            <br/>

            <div class="form-floating">
              <input type="password" class="form-control" id="floatingPassword" v-model="password" required>
              <label for="floatingPassword">Password</label>
            </div>
            
            <br/>
            <button class="w-100 btn btn-lg btn-primary" type="submit">Sign in</button>
            <p class="mt-5 mb-3 text-muted">&copy; BitByBit technologies</p>
          </form>
        </main>

      </div>
    </div>
  </div>
</template>


<script>
import axios from 'axios'
export default{
    name: 'SignIn',
    data: function(){
      return {
        email: "",
        password: ""
      }
    },
    methods: {
      signInUser: function(){
        console.log(this.email)
        console.log(this.password)

        axios.post('http://127.0.0.1:8000/user_auth/get_token/', {
          username: this.email,
          password: this.password
        })
        .then((response) => {
          let res = response.data
          let token = res.token
          localStorage.setItem('token', token)
          this.email = ""
          this.password = ""
          this.$router.push({name:'admin_panel'})
        })
        .catch((error) => {
          alert("An error occurred, please try again")
        })


      }
    },
}
  
  </script>