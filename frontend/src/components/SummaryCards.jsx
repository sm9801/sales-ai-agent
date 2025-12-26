const Card = ({ title, value }) => (
    <div style={{
        padding: "20px",
        border: "1px solid #ddd",
        borderRadius: "8px",
        minWidth: "160px"
    }}>
        <h4>{title}</h4>
        <strong>{value}</strong>
    </div>
);

const SummaryCards = ({ data }) => {
    if (!data) return null;

    return (
        <div style={{ display: "flex", gap: "20px" }}>
            <Card title="Total Revenue" value={'$${data.total_revenue}'} />
            <Card title="Total Orders" value={data.total_orders} />
            <Card title="AOV" value={'$${data.aov}'} />
            <Card title="Total Units" value={data.total_units} />
        </div>
    );
};

export default SummaryCards;

