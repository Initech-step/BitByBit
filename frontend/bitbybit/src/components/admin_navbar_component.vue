<template>
    <nav class="navbar navbar-dark bg-dark" aria-label="Dark offcanvas navbar">
        <div class="container-fluid">
            <a class="navbar-brand" href="#">BitByBit</a>
            <button class="navbar-toggler" type="button" data-bs-toggle="offcanvas" data-bs-target="#offcanvasNavbarDark" aria-controls="offcanvasNavbarDark">
                <span class="navbar-toggler-icon"></span>
            </button>
        <div class="offcanvas offcanvas-end text-bg-dark" tabindex="-1" id="offcanvasNavbarDark" aria-labelledby="offcanvasNavbarDarkLabel">
            <div class="offcanvas-header">
                <h5 class="offcanvas-title" id="offcanvasNavbarDarkLabel">User Administration</h5>
                <button type="button" class="btn-close btn-close-white" data-bs-dismiss="offcanvas" aria-label="Close"></button>
            </div>
            <div class="offcanvas-body">
            <ul class="navbar-nav justify-content-end flex-grow-1 pe-3">

                <router-link :to="{name: 'admin_panel'}">
                    <li class="nav-item">
                        <a class="nav-link active" aria-current="page" href="#">My Profile</a>
                    </li>
                </router-link>
                
                <li class="nav-item dropdown">
                    <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">Groups </a>

                    <ul class="dropdown-menu">
                        <router-link :to="{name: 'create_group'}">
                            <li><a class="dropdown-item" href="#">Create Group</a></li>
                        </router-link>

                        <router-link :to="{name: 'currently_managing'}">
                            <li><a class="dropdown-item" href="#">Manage my created group</a></li>
                        </router-link>
                        
                        <router-link :to="{name: 'sub_manage'}">
                            <li><a class="dropdown-item" href="#">Manage my admin groups</a></li>
                        </router-link>
                        
                    </ul>
                </li>

                <li class="nav-item dropdown">
                    <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">Applications </a>
                    <ul class="dropdown-menu">
                        <router-link :to="{name: 'view_application'}">
                            <li><a class="dropdown-item" href="#">Application to my group</a></li>
                        </router-link>
                        
                        <router-link :to="{name: 'groups_open'}">
                            <li><a class="dropdown-item" href="#">Groups open for applications</a></li>
                        </router-link>     
                    </ul>
                </li>

                <router-link :to="{name: 'set_managing'}">
                    <li class="nav-item">
                        <a class="nav-link" href="#">Set currently managing</a>
                    </li>
                </router-link>
                

            </ul>
            <form class="d-flex mt-3" role="search">
                <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
                <button class="btn btn-outline-success" type="submit">Search</button>
            </form>
            </div>
        </div>
        </div>
  </nav>
</template>

<script>
export default {
    name: 'AdminNavbar'
}
</script>

<style scoped>
body {
  padding-bottom: 20px;
}

.navbar {
  margin-bottom: 20px;
}
</style>