        
<template>
    <form class="form-signin" @submit.prevent="signUpUser">
      <div class="text-center mb-4">
        <img class="mb-4" src="@/assets/b3logo.png" alt="" width="72" height="76">
        <h1 class="h3 mb-3 font-weight-normal">Sign Up</h1>
        <p>Lets get You started</p>
      </div>
    

      <div class="form-label-group">
        <input type="email" id="inputEmail" class="form-control" placeholder="Email address" required v-model="email">
        <label for="inputEmail">email</label>
      </div>


      <div class="form-label-group">
        <input type="text" id="inputFName" class="form-control" placeholder="First name" required v-model="first_name">
        <label for="inputFName">First name</label>
      </div>


      <div class="form-label-group">
        <input type="text" id="inputLName" class="form-control" placeholder="Last name" required v-model="last_name">
        <label for="inputLName">Last name</label>
      </div>



      <div class="form-label-group">
        <input type="text" id="Department" class="form-control" placeholder="School department eg. accounting" required v-model="department">
        <label for="Department">Department</label>
      </div>


    
      <div class="form-label-group">
        <input type="text" id="University" class="form-control" placeholder="University" required v-model="university">
        <label for="University">University </label>
      </div>



      <div class="form-label-group">
        <input type="text" id="uniShort" class="form-control" required v-model="uni_short">
        <label for="uniShort">University short eg. (UNIUYO)</label>
      </div>


      <div class="form-label-group">
        <input type="number" id="setYear" class="form-control" placeholder="Set year" required v-model="set_year">
        <label for="setYear">Set year</label>
      </div>



      <div class="form-label-group">
        <input type="password" id="password" class="form-control" required v-model="password">
        <label for="password">Password</label>
      </div>


      <div class="form-label-group">
        <input type="password" id="confirmPassword" class="form-control" required v-model="confirm_password">
        <label for="confirmPassword">Confirm password</label>
      </div>
    
      <button class="btn btn-lg btn-primary text-white btn-block text-dark w-100" type="submit">Sign Up</button>
      <p class="mt-5 mb-3 text-muted text-center">&copy; BitByBit</p>
    </form>
</template>












<style scoped>
html,
body {
    height: 100%;
}

body {
    display: -ms-flexbox;
    display: flex;
    -ms-flex-align: center;
    align-items: center;
    padding-top: 40px;
    padding-bottom: 40px;
    background-color: #f5f5f5;
}

.form-signin {
    width: 100%;
    max-width: 420px;
    padding: 15px;
    margin: auto;
}

.form-label-group {
    position: relative;
    margin-bottom: 1rem;
}

.form-label-group input,
.form-label-group label {
    height: 3.125rem;
    padding: .75rem;
}

.form-label-group label {
    position: absolute;
    top: 0;
    left: 0;
    display: block;
    width: 100%;
    margin-bottom: 0; /* Override default `<label>` margin */
    line-height: 1.5;
    color: #495057;
    pointer-events: none;
    cursor: text; /* Match the input under the label */
    border: 1px solid transparent;
    border-radius: .25rem;
    transition: all .1s ease-in-out;
}

.form-label-group input::-webkit-input-placeholder {
    color: transparent;
}

.form-label-group input::-moz-placeholder {
    color: transparent;
}

.form-label-group input:-ms-input-placeholder {
    color: transparent;
}

.form-label-group input::-ms-input-placeholder {
    color: transparent;
}

.form-label-group input::placeholder {
    color: transparent;
}

.form-label-group input:not(:-moz-placeholder-shown) {
    padding-top: 1.25rem;
    padding-bottom: .25rem;
}

.form-label-group input:not(:-ms-input-placeholder) {
    padding-top: 1.25rem;
    padding-bottom: .25rem;
}

.form-label-group input:not(:placeholder-shown) {
    padding-top: 1.25rem;
    padding-bottom: .25rem;
}

.form-label-group input:not(:-moz-placeholder-shown) ~ label {
    padding-top: .25rem;
    padding-bottom: .25rem;
    font-size: 12px;
    color: #777;
}

.form-label-group input:not(:-ms-input-placeholder) ~ label {
    padding-top: .25rem;
    padding-bottom: .25rem;
    font-size: 12px;
    color: #777;
}

.form-label-group input:not(:placeholder-shown) ~ label {
    padding-top: .25rem;
    padding-bottom: .25rem;
    font-size: 12px;
    color: #777;
}

/* Fallback for Edge
-------------------------------------------------- */
@supports (-ms-ime-align: auto) {
    .form-label-group {
    display: -ms-flexbox;
    display: flex;
    -ms-flex-direction: column-reverse;
    flex-direction: column-reverse;
    }

    .form-label-group label {
    position: static;
    }

    .form-label-group input::-ms-input-placeholder {
    color: #777;
    }
}
</style>




<script>
import axios from 'axios'

export default{
    name: 'SignIn',
    data: function(){
        return {
            email: "",
            first_name:"",
            last_name:"",
            university:"",
            uni_short:"",
            department:"",
            password:"",
            confirm_password:"",
            set_year:""

        }
    },
    methods: {
        signUpUser: function(){
            if (this.password != this.confirm_password){
                alert("Passwords do not match")
            }else{
                axios.post('http://127.0.0.1:8000/user_auth/create_user/', {
                    first_name: this.first_name,
                    email: this.email,
                    last_name: this.last_name,
                    department: this.department,
                    school: this.university,
                    school_short_form: this.uni_short,
                    set_year: this.set_year,
                    password: this.password

                })
                .then((response) => {
                    alert("You have successfully signed up, you will get mail. Please log in.")
                    this.first_name = ""
                    this.email = ""
                    this.last_name = ""
                    this.department = ""
                    this.university = ""
                    this.uni_short = ""
                    this.set_year = ""
                    this.password = ""
                    this.confirm_password = ""
                })
                .catch((error) => {
                    alert("An error occurred")
                })
            }
        }
    }
}

</script>
