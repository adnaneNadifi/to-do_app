<template>
  <q-page class="flex flex-center">
    <div>
    <q-card class="mb-5">
       <q-card-section>
        <div>
          <q-input v-model="text" type="text" label="Enter task title" />
          <q-input v-model="text" type="text" label="Enter task description" />
        </div>
        <div class="flex justify-end pt-3 [&>*]:ml-2">
          <q-btn class="bg-green-600 text-white" icon="check" label="add"/>
          <q-btn class="bg-blue-600 text-white" icon="restart_alt" label="reset"/>
        </div>
      </q-card-section>
    </q-card>
    <q-card class="w-[500px]">
        <q-list class="pl-2" bordered separator>
          <q-item >
            <q-item-section class="flex">
              <div class="py-2 text-xl">
                <q-item-label overline>OVERLINE</q-item-label>
                <q-item-label>Item with </q-item-label>
              </div>
              <div class="[&>*]:p-2 text-xl flex justify-end">
                <q-icon class="text-green-600 cursor-pointer" name="done"  clickable v-ripple/>
                <q-icon  @click="prompt = true" class="text-blue-600 cursor-pointer" name="edit" clickable v-ripple />
                <q-icon class="text-red-600 cursor-pointer" name="close" clickable v-ripple />
              </div>
            </q-item-section>
          </q-item>
        </q-list>
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
    </div>
  </q-page>
</template>

<script setup>
import { ref } from 'vue'

const prompt = ref(false)

</script>
