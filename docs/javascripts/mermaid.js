document$.subscribe(function () {
  if (typeof mermaid === "undefined") {
    return;
  }

  function ensureDiagramShell(diagram, index) {
    const existingShell = diagram.closest(".diagram-shell");
    if (existingShell) {
      return existingShell;
    }

    const shell = document.createElement("div");
    shell.className = "diagram-shell";
    shell.dataset.diagramIndex = String(index + 1);

    const controls = document.createElement("div");
    controls.className = "diagram-shell__controls";

    const button = document.createElement("button");
    button.className = "diagram-shell__toggle";
    button.type = "button";
    button.setAttribute("aria-expanded", "false");
    button.textContent = "View diagram full-width";
    button.addEventListener("click", function () {
      const expanded = shell.classList.toggle("diagram-shell--full-width");
      button.setAttribute("aria-expanded", expanded ? "true" : "false");
      button.textContent = expanded
        ? "Return to standard width"
        : "View diagram full-width";
    });

    controls.appendChild(button);
    diagram.parentNode.insertBefore(shell, diagram);
    shell.appendChild(controls);
    shell.appendChild(diagram);
    return shell;
  }

  document.querySelectorAll(".mermaid").forEach(function (diagram, index) {
    ensureDiagramShell(diagram, index);
  });

  mermaid.initialize({
    startOnLoad: false,
    securityLevel: "strict",
    theme: "neo",
    fontFamily: "Helvetica, Arial, sans-serif",
    flowchart: {
      curve: "linear",
      htmlLabels: true,
    },
  });

  mermaid.run({
    querySelector: ".mermaid",
  });
});
