<template>
  <div class='layout'>
      <el-container>
          <el-header>
              <Header></Header>
          </el-header>
          <el-container class='content'>
              <el-aside width='150px'>
                  <AsideNav></AsideNav>
              </el-aside>
              <el-main>
                  <router-view></router-view>
              </el-main>
          </el-container>
          <el-footer>
              <Footer></Footer>
          </el-footer>
          <div>
              index页面
          </div>
      </el-container>
  </div>
</template>

<script>
import Header from './components/Header';
import AsideNav from './components/AsideNav';
import Footer from './components/Footer';
export default {
    name: 'Layout',
    components: {
        Header,
        AsideNav,
        Footer
    }
}
</script>

<style scoped>
    .layout{
        position: relative;
        width: 100%;
        height: 100%;
    }
    .el-header{
        width: 100%;
        height: 60px;
    }
    .el-footer{
        position: absolute;
        bottom: 0px;
        left: 0px;
        width: 100%;
    }
    .content{
        width: 100%;
        position: absolute;
        top: 70px;
        bottom: 60px;
        border-bottom: 1px solid #0f4bcc;
        border-bottom: 10px;
    }
    .el-menu{
        border:none;
    }
    .el-aside{
        height: 100%;
        border-right: solid 1px #56389b;
    }
    
</style>