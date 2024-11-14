// Load the data from CSV (adjust path as needed)
d3.csv("data/Playoffs.csv").then(function (data) {
    // Prepare the data by calculating 3PT per game
    data.forEach(d => {
        d["3PT_PG"] = +d.FG3M / +d.GP;  // Calculating 3-point field goals per game
    });

    // Filter for the top 30 players based on 3PT per game
    data = data.sort((a, b) => b["3PT_PG"] - a["3PT_PG"]).slice(0, 30);

    // Set up chart dimensions
    const margin = { top: 20, right: 30, bottom: 60, left: 150 },
        width = 800 - margin.left - margin.right,
        height = 600 - margin.top - margin.bottom;

    // Create SVG element
    const svg = d3.select("#chart")
        .append("svg")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
        .append("g")
        .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

    // Set up scales
    const x = d3.scaleLinear()
        .domain([0, d3.max(data, d => d["3PT_PG"])])
        .range([0, width]);

    const y = d3.scaleBand()
        .domain(data.map(d => d.PLAYER))
        .range([0, height])
        .padding(0.1);

    // Add bars
    svg.selectAll(".bar")
        .data(data)
        .enter()
        .append("rect")
        .attr("class", "bar")
        .attr("x", 0)
        .attr("y", d => y(d.PLAYER))
        .attr("width", d => x(d["3PT_PG"]))
        .attr("height", y.bandwidth());

    // Add Y axis
    svg.append("g")
        .call(d3.axisLeft(y))
        .attr("class", "axis-label");

    // Add X axis
    svg.append("g")
        .call(d3.axisBottom(x))
        .attr("transform", "translate(0," + height + ")")
        .attr("class", "axis-label")
        .append("text")
        .attr("fill", "#000")
        .attr("x", width / 2)
        .attr("y", 40)
        .attr("text-anchor", "middle")
        .text("3-Point Field Goals per Game");
});