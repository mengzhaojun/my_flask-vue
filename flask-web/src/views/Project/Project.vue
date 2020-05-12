<template>
  <div>
    <el-breadcrumb separator="/">
      <el-breadcrumb-item :to="{ path: '/' }">首页</el-breadcrumb-item>
      <el-breadcrumb-item>项目列表</el-breadcrumb-item>
    </el-breadcrumb>
    <div>
      <span>
        <el-button type="primary" icon="el-icon-circle-plus-outline" @click="dialogFormVisible = true">添加项目</el-button>
      </span>
      <el-dialog title="收货地址" :visible.sync="dialogFormVisible">
        <el-form :model="form">
          <el-form-item label="项目名称： " :label-width="formLabelWidth">
            <el-input v-model="form.name" auto-complete="off"></el-input>
          </el-form-item>
          <el-form-item label="项目描述： " :label-width="formLabelWidth">
            <el-input v-model="form.region" auto-complete="off"></el-input>
          </el-form-item>
          <el-form-item label="版本号： " :label-width="formLabelWidth">
            <el-input v-model="form.version" auto-complete="off"></el-input>
          </el-form-item>
          <!-- <el-form-item label="活动区域" :label-width="formLabelWidth">
            <el-select v-model="form.region" placeholder="请选择活动区域">
              <el-option label="区域一" value="shanghai"></el-option>
              <el-option label="区域二" value="beijing"></el-option>
            </el-select>
          </el-form-item> -->
        </el-form>
        <div slot="footer" class="dialog-footer">
          <el-button @click="dialogFormVisible = false">取 消</el-button>
          <!-- <el-button type="primary" @click="dialogFormVisible = false">确 定</el-button> -->
          <el-button type="primary"  @click="add_project()">确 定</el-button>
        </div>
      </el-dialog>
    </div>
    <div class="table">
      <el-table
        ref="multipleTable"
        :data="tableData3"
        tooltip-effect="dark"
        border
        style="width: 100%"
      >
        <el-table-column type="selection" width="55"></el-table-column>
        <el-table-column prop="name" label="项目名称" width="200"></el-table-column>
        <el-table-column prop="region" label="项目描述" width="580"></el-table-column>
        <el-table-column prop="version" label="项目版本号" width="250"></el-table-column>
        <el-table-column prop="datetime" label="项目创建时间" width="250"></el-table-column>
      </el-table>
      <div style="margin-top: 20px">
        <el-button @click="todelete()">删除</el-button>
        <!-- <el-button @click="toggleSelection()">取消选择</el-button> -->
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import Qs from 'qs';

export default {
  name: "project",
  data() {
    return {
      input: "",
      tableData3: [
        {
          date: "2016-05-03",
          name: "王小虎",
          address: "上海市普陀区金沙江路 1518 弄"
        }, 
      ],
      dialogTableVisible: false,
      dialogFormVisible: false,
      form: {
        name: '',
        region: '',
        version: '',
        datetime: '',
        date1: '',
        date2: '',
        delivery: false,
        type: [],
        resource: '',
        desc: ''
      },
      formLabelWidth: '120px'
    };
  },
  created() {
      this.project_list();
  },
  methods: {
    add_project: function(){
      // console.log(this.form.name)
      var data = Qs.stringify({
        "name": this.form.name,
        "region": this.form.region,
        "version": this.form.version
        })
      axios.post('http://127.0.0.1:5000/add_project', data)
      .then((res)=>{
        // console.log(res.data)
      })
      .catch((error)=>{
        console.log(error)
      })
      this.dialogFormVisible = false;
      this.$router.go(0)
    },

    project_list: function(){
      // var self = this;
      axios.get('http://127.0.0.1:5000/project_list')
        .then((res)=>{
          console.log(this.tableData3)
          this.tableData3 = res.data.data;
          console.log(this.tableData3);
        })
        .catch((error)=>{
          console.log(error)
        })
    }
  }
};
</script>

<style scoped>
.el-button {
  float: left;
  margin-top: 20px;
  margin-bottom: 20px;
}
</style>