import React from 'react';
import { Link } from 'react-router';

var ResourceTableEntry = React.createClass({

    render: function() {
        var resource = this.props.resource;
        var columnKeys = this.props.columnKeys;
        var columnLinks = this.props.columnLinks;
        return (
            <tr>
                { this.status(resource) }
                { this.columns(resource, columnKeys, columnLinks) }
            </tr>
        );
    },

    columns: function(resource, columnKeys, columnLinks) {
        var result = [];
        for (var i = 0; i < columnKeys.length; i++) {
            var key = columnKeys[i];
            var val = resource[key];
            if (columnLinks[key]) {
                var link = columnLinks[key](resource);
                result.push(
                    <td key={i} className="rs-table-link">
                        <Link to={link}> {val} </Link>
                    </td>
                );
            } else if (key === "criteria"){
                var threshold = val["threshold"];
                var sample_size = val["result_sample_size"];
                result.push(
                    <td key={i} className="rs-table-link">{threshold}% of the {sample_size} most results results must pass</td>
                );
            } else {
                result.push(
                    <td key={i} className="rs-table-link">{val}</td>
                );
            }
        }
        return result;
    },

    status:  function(resource) {
        if (resource["health"] === "RED" || resource["status"] === "fail") {
            return <td className="rs-table-status rs-table-status-error"> </td>
        } else {
            return <td className="rs-table-status rs-table-status-ok"> </td>
        }
    }


});

export default ResourceTableEntry;
