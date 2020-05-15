<template>
  <div>
    <el-breadcrumb separator="/">
      <el-breadcrumb-item :to="{ path: '/' }">首页</el-breadcrumb-item>
      <el-breadcrumb-item :to="{ path: '/project'}">项目列表</el-breadcrumb-item>
      <el-breadcrumb-item>模块列表</el-breadcrumb-item>
    </el-breadcrumb>
    <div>
      <span @click="get_projectlist()">
        <el-button
          id="add_module"
          type="primary"
          icon="el-icon-circle-plus-outline"
          @click="dialogFormVisible = true"
        >添加模块</el-button>
      </span>
    </div>
    <el-dialog title="添加模块" :visible.sync="dialogFormVisible">
      <el-form :model="form">
        <el-form-item label="模块名称： " :label-width="formLableWidth">
          <el-input v-model="form.name" auto-complete="off"></el-input>
        </el-form-item>
        <el-form-item label="模块描述： " :label-width="formLableWidth">
          <el-input v-model="form.region" auto-complete="off"></el-input>
        </el-form-item>
        <el-form-item label="所属项目： " :label-width="formLableWidth">
          <el-select v-model="value4" clearable placeholder="请选择">
            <el-option
              v-for="item in options"
              :key="item.value"
              :label="item.label"
              :value="item.value"
            ></el-option>
          </el-select>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="dialogFormVisible = false">取消</el-button>
        <el-button type="primary" @click="add_module()">取消</el-button>
      </div>
    </el-dialog>
    <div class="table">
      <el-table
        ref="multipleTable"
        :data="tableData3"
        tooltip-effect="dark"
        border
        style="width: 100%"
      >
        <el-table-column type="selection" width="55"></el-table-column>
        <el-table-column prop="name" label="模块名称" width="180"></el-table-column>
        <el-table-column prop="region" label="模块描述" width="350"></el-table-column>
        <el-table-column prop="project_name" label="所属项目"></el-table-column>
        <el-table-column prop="datetime" label="模块创建时间" width="250"></el-table-column>
        <el-table-column label="操作">
          <template slot-scope="scope">
            <el-button size="mini" type="success" @click="handleIn(scope.$index, scope.row)">进入</el-button>
            <el-button size="mini" type="danger" @click="handleDelete(scope.$index, scope.row)">删除</el-button>
          </template>
        </el-table-column>
      </el-table>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import Qs from "qs";

export default {
  inject: ["reload"],
  name: "module",
  data() {
    return {
      input: "",
      tableData3: [
        {
          datetime: "2016-05-03",
          name: "王小虎",
          region: "上海市普陀区金沙江路 1518 弄",
          project_name: "project_name"
        }
      ],
      dialogFormVisible: false,
      formLableWidth: "120px",
      form: {
        name: "",
        region: "",
        project_name: ""
      },
      options: [],
        //   value: '选项1',
        //   label: '黄金糕'
        // }, {
        //   value: '选项2',
        //   label: '双皮奶'
        // }, {
        //   value: '选项3',
        //   label: '蚵仔煎'
        // }, {
        //   value: '选项4',
        //   label: '龙须面'
        // }, {
        //   value: '选项5',
        //   label: '北京烤鸭'
        // }],
        value4: ''
    }
  },
  created() {
    this.module_list();
  },

  methods: {
    module_list: function() {
      // var self = this;
      axios
        .get("http://127.0.0.1:5000/moduleList", {
          params: {
            p_name: this.$route.query.p_name
          }
        })
        .then(res => {
          console.log(this.$route.query.p_name);
          // console.log(this.tableData3)
          this.tableData3 = res.data.data;
          // console.log(this.tableData3);
        })
        .catch(error => {
          console.log(error);
        });
    },

    get_projectlist: function(){
      axios.get("http://127.0.0.1:5000/projectlist")
        .then((res)=>{
          this.options = res.data.data;
        })
        .catch((error)=>{
          console.log(error)
        })
    }
  }  
}
</script>

<style scoped>
#add_module {
  float: left;
  margin-top: 20px;
  margin-bottom: 20px;
}
</style>