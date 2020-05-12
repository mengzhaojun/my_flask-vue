<template>
  <el-row class='tac'>
      <el-col :span='24'>
          <el-menu
            :default-active='defaultActive'
            class="el-men-vertical-demo"
            @open="handleOpen"
            @close="handleClose"
          >
          <router-link to="project">
              <el-menu-item index="project">
                  <i class="el-icon-location"></i>
                  <span slot="title">项目列表</span>
              </el-menu-item>
          </router-link>
          <router-link to="module">
              <el-menu-item index="module">
                  <i class="el-icon-news"></i>
                  <span slot="title">模块列表</span>
              </el-menu-item>
          </router-link>
          <router-link to="case">
              <el-menu-item index="case">
                  <i class="el-icon-tickets"></i>
                  <span slot="title">用例列表</span>
              </el-menu-item>
          </router-link>
          <router-link to="setting">
              <el-menu-item index="setting">
                  <i class="el-icon-setting"></i>
                  <span slot="title"> 设 置 </span>
              </el-menu-item>
          </router-link>
          </el-menu>
      </el-col>
  </el-row>
</template>

<script>
export default {
    name: 'AsideNav',
    components: {

    },
    data(){
        return{

        };
    },
    computed:{
        defaultActive(){
            return this.$route.path
        }
    },
    methods: {
        handleOpen(index){
            console.log(index)
        },
        handleClose(index){
            console.log(index)
        }
    }
}
</script>

<style scoped>
.tac{
    height: 100%;
}
</style>