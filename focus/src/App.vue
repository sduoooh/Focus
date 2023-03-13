<script setup>
import { ref } from "vue"
import axios from 'axios'

const chatList = ref([{ "role": "AI", "text": "您好，您目前尚未登录，请输入api后连接openai." }, 
])

const question = ref("")
const status = ref(false)
const loginStatus = ref(false)

async function login(){
  if (!status.value){
  if (question.value === "") {
    console.warn("Can not send the empty imformation.")
    return
  }
  status.value = true
  chatList.value.push({"role":"user","text":question.value})
  await axios.post("http://127.0.0.1:8000/login",{"userAPI":question.value})
  .then((response)=>{
    console.warn("登录成功！以下是详细信息：")
    console.log(response)
    chatList.value.push({"role":"system", "text":"登陆成功！"})
    chatList.value.push({"role":"AI", "text": response["data"]["msg"]['choices'][0]['message']['content']})
    loginStatus.value = true
  })
  .catch((error)=>{
    console.warn("输入了错误的api。")
    console.log(error)
    chatList.value.push({"role":"system", "text":"输入了错误的api。"})
  })
  question.value = ""
  status.value = false
  }
}

async function send(){
  if (!status.value){
  if (question.value === "") {
    console.warn("Can not send the empty imformation.")
    return
  }
  status.value = true
  chatList.value.push({"role":"user","text":question.value})
  await axios.post("http://127.0.0.1:8000/chat",{"msg":question.value,"model":"chat",})
  .then((response)=>{
    console.warn("成功返回信息，以下是详细信息：")
    console.log(response)
    chatList.value.push({"role":"AI", "text": response["data"]["msg"]})
  })
  .catch((error)=>{
    console.warn("服务器掉线了")
    chatList.value.push({"role":"system", "text":"服务器掉线了"})
  })
  question.value = ""
  status.value = false
  }
}

</script>

<template>
  <div>
    <div
      style="display: flex;align-items: flex-end; flex-wrap: wrap; width: 100vw; align-content: flex-end; position: absolute; margin-top: 100px;">
      <div class="chatDiv" v-for="text in chatList"
        :style="color = (text) => { return text.role == user ? black : white; }">
        <div style="margin: 10px;margin-left: 50px;">
         <p>{{text.role}} :</p><p>{{ text.text }}</p>
        </div>
      </div>
      <div style="height: 20vh; width:80vw;"></div>
    </div>
    <div style="height:20vh;width: 80vw;position: fixed; bottom: 0;">
      <div  style="margin-top: 10vh;">
        <input
          v-model="question"
          class="chatDiv" 
          style="
            line-height: 25px;
            font-size: 15px;
            text-indent: 15px;"
        > 
        <div @click="loginStatus?send():login()" style="border-radius: 25px;width:20px;height:20px;background-color: brown;margin-left: 92vw; position: relative; bottom: 3.5vh;"></div>
      </div>

    </div>
  </div>
</template>

<style scoped>
.chatDiv {
  width: 80vw;
  margin: 10px;
  margin-left: 10vw;

  border-radius: 25px;
  box-shadow: 5px 5px 5px #888888;

  background-color: white;
}

.black {
  color: black;
}

.white {
  background-color: greenyellow;
  color: white;
}</style>
