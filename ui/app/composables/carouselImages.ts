import { ref } from 'vue';

export const useCarouselImages = () => {
  const images = [
    "/img1.jpg",
    "/img2.jpg",
    "/img3.jpg"
  ];

  const activeIdx = ref(0);

  const nextSlide = () => {
    activeIdx.value = (activeIdx.value + 1) % images.length;
  };

  const prevSlide = () => {
    activeIdx.value =
      activeIdx.value === 0
        ? images.length - 1
        : activeIdx.value - 1;
  };

  return {
    images,
    activeIdx,
    nextSlide,
    prevSlide
  };
};