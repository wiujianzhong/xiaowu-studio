(() => {
  const hostname = window.location.hostname.toLowerCase();
  const isXiaowuDomain =
    hostname === "xiaowustudio.cn" || hostname.endsWith(".xiaowustudio.cn");

  if (!isXiaowuDomain || document.querySelector("script[data-cf-beacon]")) {
    return;
  }

  const beacon = document.createElement("script");
  beacon.type = "module";
  beacon.src = "https://static.cloudflareinsights.com/beacon.min.js";
  beacon.dataset.cfBeacon = JSON.stringify({
    token: "23236c01e042430291a238cc3064911b",
  });
  document.head.appendChild(beacon);
})();
