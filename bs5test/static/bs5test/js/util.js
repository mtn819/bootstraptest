const addClassTemp = (el, className, dur=2000) => {
    el.classList.add(className);
    setTimeout(() => el.classList.remove(className), dur)
}