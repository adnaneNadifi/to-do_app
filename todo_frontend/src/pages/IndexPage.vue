<template>
  <q-page class="flex flex-center">
    <div>
    <q-card class="mb-5">
       <q-card-section>
        <div>
          <q-input v-model="task_title" type="text" label="Enter task title" />
          <q-input v-model="task_description" type="text" label="Enter task description" />
        </div>
        <div class="flex justify-end pt-3 [&>*]:ml-2">
          <q-btn  @click="addTaskData(task_title,task_description)" class="bg-green-600 text-white" icon="check" label="Add task"/>
          <q-btn @click="Reset" class="bg-blue-600 text-white" icon="restart_alt" label="reset"/>
        </div>
      </q-card-section>
    </q-card>
    <q-card class="w-[500px]">
      <!-- task list -->
      <q-list  bordered separator>

        <q-item v-for="task in todo_tasks " :key="task.id" >
          
          <q-item-section class="flex">
            <div class="py-2 text-xl">
              <q-item-label overline>{{task.title}}</q-item-label>
              <q-item-label>{{task.description}} </q-item-label>
            </div>
            <div class="[&>*]:p-2 text-xl flex justify-end">
              <q-icon class="text-green-600 cursor-pointer" name="done"  clickable v-ripple/>
              <q-icon  @click="prompt = true" class="text-blue-600 cursor-pointer" name="edit" clickable v-ripple />
              <q-icon @click="confirm = true" class="text-red-600 cursor-pointer" name="close" clickable v-ripple />
            </div>
          </q-item-section>
          <!-- confirm model -->
          <q-dialog v-model="confirm" persistent>
            <q-card>
              <q-card-section class="row items-center">
                <q-avatar icon="warning" class="text-red-600 "  />
                <span class="q-ml-sm">Are you sure you want to delete this task!</span>
              </q-card-section>

              <q-card-actions align="right">
                <q-btn :loading="loading" class="bg-red-600 text-white" @click="deleteTaskData(task.id)" label="Remove task"  v-close-popup/>
                <q-btn flat label="Cancel" color="primary" v-close-popup />
              </q-card-actions>
            </q-card>
          </q-dialog>
        
        </q-item>
      
      </q-list>

      <!-- update popup -->
      <q-dialog v-model="prompt" persistent>
          <q-card style="min-width: 350px">
            <q-card-section>
              <div class="text-h6">Your address</div>
            </q-card-section>

            <q-card-section class="q-pt-none">
              <q-input dense v-model="address" autofocus @keyup.enter="prompt = false" />
            </q-card-section>

            <q-card-actions align="right" class="text-primary">
              <q-btn flat label="Cancel" v-close-popup />
              <q-btn flat label="Add address" v-close-popup />
            </q-card-actions>
        </q-card>
      </q-dialog>
    </q-card>
      
    <q-card v-if='Object.keys(error).length === 0' class="my-card p-3">
      <p class=" text-lg bold  text-red-500">{{error.error_title}}</p>
      <p class="  text-red-500">{{error.error_description}}</p>
    </q-card>
    </div>
  </q-page>
</template>

<script setup>

import { onMounted, reactive, ref } from 'vue'
import axios from 'axios'

const prompt = ref(false)
const confirm = ref(false)

const task_title = ref('')
const task_description = ref('')


let todo_tasks = ref([])
const error = reactive({
   error_title : '',
   error_description : '',
})

onMounted(getTasksData)

function getTasksData() {
  axios
    .get('http://localhost:8000/api/todos/')
    .then((response) => {
      todo_tasks.value = response.data
    })
    .catch((err) => {
      error.error_title="Somthing's wrong here....."
      error.error_description='No task found!'
    })

} 

function deleteTaskData(id) {
  axios
    .delete(`http://localhost:8000/api/todos/${id}`)
    .then((response) => {
      getTasksData()
    })
    .catch((err) => {
      error.error_title="Somthing's wrong here....."
      error.error_description='somthing happend'
  })
  
}

function addTaskData(title, description) {
  
  const task = {
    title:title,
    description: description,
    is_completed: false,
  }

  axios.post('http://localhost:8000/api/todos/',task)
    .then((response) => {
      Reset()
      getTasksData()
    })
    .catch((err) => {
      console.log(err);
  })
}

function Reset () {
  task_title.value = null
  task_description.value = null

}
</script>
