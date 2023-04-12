import React, { useState, useEffect } from 'react';

import Song from "../components/Song";
import "./Chart.css"

const Chart = () => {
    const [chart, setChart] = useState([])

    useEffect(() => {
        fetchChart()
    }, [])

    const fetchChart = function() {
        fetch("https://itunes.apple.com/gb/rss/topsongs/limit=20/json")
        .then(response => response.json())
        .then(data => setChart(data.feed.entry))
      }
    
    

    return ( 
        <>
            <h1>Today's Top 20 from iTunes</h1>
            <ol type="1" className='chart'>
                <Song chart={chart}/>
            </ol>
        </>
     );
}

 
 
export default Chart;