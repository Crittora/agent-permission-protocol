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
    theme: "base",
    fontFamily: "Helvetica, Arial, sans-serif",
    flowchart: {
      curve: "linear",
      htmlLabels: true,
    },
    themeVariables: {
      background: "#0b1220",
      primaryColor: "#111827",
      primaryTextColor: "#f8fafc",
      primaryBorderColor: "#38bdf8",
      lineColor: "#94a3b8",
      secondaryColor: "#172033",
      secondaryTextColor: "#e2e8f0",
      secondaryBorderColor: "#60a5fa",
      tertiaryColor: "#1f2937",
      tertiaryTextColor: "#f8fafc",
      tertiaryBorderColor: "#22d3ee",
      mainBkg: "#111827",
      secondBkg: "#172033",
      tertiaryBkg: "#1f2937",
      nodeBorder: "#38bdf8",
      clusterBkg: "#0f172a",
      clusterBorder: "#334155",
      defaultLinkColor: "#94a3b8",
      titleColor: "#f8fafc",
      edgeLabelBackground: "#0f172a",
      textColor: "#e2e8f0",
      actorBkg: "#111827",
      actorBorder: "#38bdf8",
      actorTextColor: "#f8fafc",
      actorLineColor: "#475569",
      signalColor: "#e2e8f0",
      signalTextColor: "#e2e8f0",
      labelBoxBkgColor: "#111827",
      labelBoxBorderColor: "#38bdf8",
      labelTextColor: "#f8fafc",
      loopTextColor: "#f8fafc",
      noteBkgColor: "#1e293b",
      noteBorderColor: "#60a5fa",
      noteTextColor: "#e2e8f0",
      activationBorderColor: "#22d3ee",
      activationBkgColor: "#0f172a",
      sequenceNumberColor: "#0b1220",
    },
  });

  mermaid.run({
    querySelector: ".mermaid",
  });
});
