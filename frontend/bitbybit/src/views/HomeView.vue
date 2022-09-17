<script>
import NavbarComponent from '@/components/navbar.vue'
import BannerComponent from '@/components/banner.vue'
import FooterComponent from '@/components/footer.vue'

export default{
  name: 'HomeView',
  components: {
    NavbarComponent,
    BannerComponent,
    FooterComponent
  }
}

</script>

<template>
  <main>
    <NavbarComponent />
    <BannerComponent />
    <FooterComponent />
  </main>
</template>
