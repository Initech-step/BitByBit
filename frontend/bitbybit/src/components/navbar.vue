<template>
  <div class="container">
    <header class="d-flex flex-wrap justify-content-centery py-3 mb-4 border-bottom">
      <a href="/" class="d-flex align-items-center mb-3 mb-md-0 me-md-auto text-dark text-decoration-none">
        <img alt="logo" class="logo bi me-2" src="@/assets/b3logo.png" width="45" height="40" />
        <span class="fs-4">BitByBit</span>
      </a>

      <ul class="nav nav-pills">
        <li class="nav-item text-warning"><a href="#" class="nav-link active" aria-current="page">Home</a></li>
        
        <router-link :to="{name: 'search'}">
          <li class="nav-item"><a class="nav-link" href="#">Find a group</a></li>
        </router-link>
        

        <router-link :to="{name: 'signup'}">
          <li class="nav-item"><a class="nav-link" href="#">Sign Up</a></li>
        </router-link>
        
        <router-link :to="{name: 'signin'}">
          <li class="nav-item"><a class="nav-link" href="#">Sign In</a></li>
        </router-link>

        <router-link :to="{name: 'admin_panel'}">
          <li class="nav-item"><a class="nav-link" href="#">Panel</a></li>
        </router-link>
          
      </ul>
    </header>
  </div>
</template>


<script>
export default {
 name: 'NavbarComponent'   
}
</script>

<style scoped>
</style>