<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png">
    <Myhome msg="Welcome to Your Vue.js App"/>
  </div>
</template>

<script>
// @ is an alias to /src
import Myhome from '@/components/Myhome.vue'

export default {
  name: 'About',
  components: {
    Myhome
  }
}
</script>
