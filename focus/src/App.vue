<script setup>
import { ref } from "vue"

const chatList = ref([{ "role": "AI", "text": "您好，我是您的信息助手，请输入相应的指令。" }, 
])

const question = ref("")
const status = ref(false)

function send(){
  if (!status.value){
  status.value = true
  chatList.value.push({"role":"user","text":question.value})
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
        <div @click="send" style="border-radius: 25px;width:20px;height:20px;background-color: brown;margin-left: 92vw; position: relative; bottom: 3.5vh;"></div>
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
