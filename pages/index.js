// fetch data
fetch("data.json")
  .then((response) => {
    return response.json();
  })
  .then((data) => main(data.data));

// main function
function main(data) {
  const temp = [];
  for (let i = 0; i < data.length; i += 3) {
    temp.push(data.slice(i, i + 3));
  }
  temp.forEach((row) => {
    document.querySelector("body .img-column").appendChild(render_row(row));
  });
}

function render_row(row) {
  const img_row = document.createElement("div");
  img_row.className = "img-row";
  row.forEach((element) => {
    const img_element = document.createElement("div");
    img_element.className = "img-element";

    // header
    const header = document.createElement("h1");
    header.innerText = element.title;

    // image
    const image = document.createElement("img");
    image.src = element.path + element.name;
    image.alt = "image";
    image.addEventListener("error", (event) => {
      event.target.src = "404.png";
      event.target
        .closest(".img-element")
        .querySelectorAll("button")
        .forEach((but) => {
          but.disabled = true;
        });
    });

    // button
    const img_buttons = document.createElement("div");
    const img_button1 = document.createElement("button");
    const img_button2 = document.createElement("button");
    img_buttons.className = "img-buttons";
    img_button1.innerText = "复制链接";
    img_button2.innerText = "下载截图";
    img_buttons.appendChild(img_button1);
    img_buttons.appendChild(img_button2);
    img_button1.addEventListener("click", () => {
      navigator.clipboard.writeText(element.link);
      img_button1.title = "复制";
      Fnon.Alert.Dark("复制成功", "操作提醒", "OK", () => {});
    });
    img_button2.addEventListener("click", () => {
      let a_tag = document.createElement("a");
      a_tag.href = element.path + element.name;
      a_tag.download = element.name;
      a_tag.click();
      a_tag.remove();
    });

    // append elements
    img_element.appendChild(header);
    img_element.appendChild(image);
    img_element.appendChild(img_buttons);
    img_row.appendChild(img_element);
  });
  return img_row;
}
