<script lang="ts" setup>
import { onMounted, ref } from "vue";

const props = defineProps<{
  setActiveCategory: (name: string) => void;
}>();

const categoryName = ref("");
onMounted(() => {
  const clickables = document.querySelectorAll("*[data-clickable='true']");
  const tagTextList = document.querySelectorAll("#etiquetes text");

  // Adjust the translateY for the text in the tags
  tagTextList.forEach((text) => {
    // eslint-disable-next-line @typescript-eslint/ban-ts-comment
    //@ts-ignore
    (text as HTMLElement).transform.baseVal[0].matrix.f += 4;
  });

  for (const clickable of clickables) {
    (clickable as HTMLElement).addEventListener(
      "click",
      (event: MouseEvent) => {
        if (!event.target) return;
        const elem = event.currentTarget as HTMLElement;
        event.preventDefault();
        event.stopPropagation();
        if (elem.dataset) {
          categoryName.value = elem.dataset.categoryName ?? "";
          props.setActiveCategory(categoryName.value);
        }
      }
    );
  }
});
const noiseFrequency = ref(1.0);
const numOctaves = ref(3);
setInterval(() => {
  noiseFrequency.value = Math.random() * 0.1 + 0.2;
}, 200);
</script>
<template></template>
<style scoped>
svg {
  top: -100px;
  position: absolute;
  fill: var(--black);
}
</style>
